from __future__ import absolute_import, division

from datetime import date, timedelta
import time

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

class CountUsersView(APIView):
    """
    Returns the counts of users for the day and the total up to today.
    If a date is specified, it will return fo that date. 
    If a range is specified, it will return a value for each date in the range. 

    * Only admin users are able to access this view.
    """
    permission_classes = (permissions.IsAdminUser,)

    def _get_user_counts(self, start_date, end_date):
        data_to_return = []
        while start_date <= end_date:
            inner_data = {}
            inner_data['timestamp'] = time.mktime(start_date.timetuple())
            # Since date returns at midnight, add a day but count it for the previous day
            # e.g. Looking for user counts for October 10, date(YEAR, 10, 10) would result
            # in a date object for 10/10 at midnight, which won't include users for that date.
            # To get users for 10/10, make the query date 10/11, and query on users LESS THAN
            # that date (10/10 at 11:59pm)
            start_date = start_date + timedelta(days=1)
            inner_data['daily_users'] = User.objects.filter(date_joined__gte=start_date-timedelta(days=1), date_joined__lt=start_date).count()
            inner_data['total_users'] = User.objects.filter(date_joined__lt=start_date).count()
            data_to_return.append(inner_data)
        return data_to_return

    def get(self, request, format=None):
        """
        Returns counts of users based on date ranges.
        """
        queries = request.GET
        start_time = queries.get('start_date', time.mktime(date.today().timetuple()))
        end_time = queries.get('end_date', time.mktime(date.today().timetuple()))
        start_date = date.fromtimestamp(float(start_time))
        end_date = date.fromtimestamp(float(end_time))

        if end_date < start_date:
            return Response(data={'error': 'End date cannot be before start date.'}, status=status.HTTP_400_BAD_REQUEST)

        user_counts = self._get_user_counts(start_date, end_date)

        return Response(user_counts)