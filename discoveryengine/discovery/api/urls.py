"""
    API URLs for Discovery
"""
from __future__ import absolute_import

from django.conf.urls import include, url
from rest_framework import routers

from .views import RatingViewSet

# Routers
router = routers.SimpleRouter()
router.register(r'ratings', RatingViewSet, base_name='rating')

# URLs
urlpatterns = [
    url(r'^', include(router.urls)),
]
