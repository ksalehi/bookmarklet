from __future__ import absolute_import

from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Rating

class UserSerializer(serializers.ModelSerializer):

    orcid = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'email',
            'orcid',
        )

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
