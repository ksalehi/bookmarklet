from __future__ import absolute_import

from rest_framework import permissions, status, viewsets, mixins
from rest_framework.response import Response

class ProvideEmailViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):

    def create(self, request):
        user = request.user
        data = request.POST
        permission_classes = [permissions.IsAuthenticated]

        email = data.get('email', None)
        if email:
            user.email = data.get('email')
            user.save()
            return Response()
        return Response(status=status.HTTP_400_BAD_REQUEST)
