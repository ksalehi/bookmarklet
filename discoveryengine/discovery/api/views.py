from __future__ import absolute_import, division

from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from widget.models import Version

from ..models import Question, Manuscript, Rating
from .serializers import RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    model = Rating
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Rating.objects.filter(user=user)

    def create(self, request):
        user = request.user
        data = request.POST
        version = Version.objects.get()

        # if not all([data.get('doi', None), data.get('dv', None), data.get('ac', None), data.get('cr', None), data.get('ex', None),]):
        if not data.get('doi', None):
            raise ParseError("Missing DOI")
        if not data.get('dv', None):
            raise ParseError("Missing Discovery Value")
        if not data.get('ac', None):
            raise ParseError("Missing Accountability")
        if not data.get('cr', None):
            raise ParseError("Missing Concreteness")
        if not data.get('ex', None):
            raise ParseError("Missing Expertise")

        manuscript, created = Manuscript.objects.get_or_create(doi=data["doi"])

        # Get the questions
        dvq = Question.objects.get(category='DV')
        acq = Question.objects.get(category='AC')
        crq = Question.objects.get(category='CR')
        exq = Question.objects.get(category='EX')

        # Get the values
        dvv = int(data.get('dv'))
        acv = int(data.get('ac'))
        crv = int(data.get('cr'))
        exv = int(data.get('ex'))

        # Create the objects
        dvr = Rating.objects.create(user=user, question=dvq, manuscript=manuscript, version=version, value=dvv/100)
        acr = Rating.objects.create(user=user, question=acq, manuscript=manuscript, version=version, value=acv/100)
        crr = Rating.objects.create(user=user, question=crq, manuscript=manuscript, version=version, value=crv/100)
        exr = Rating.objects.create(user=user, question=exq, manuscript=manuscript, version=version, value=exv/100)

        # Return response
        return Response(status=status.HTTP_201_CREATED)

    ###################################
    ##### NO DESTRUCTIVE METHODS ######
    ###################################
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
