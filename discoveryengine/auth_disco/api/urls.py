"""
    API URLs for Discovery
"""
from __future__ import absolute_import

from django.conf.urls import include, url
from rest_framework import routers

from .views import ProvideEmailViewSet

# Routers
router = routers.SimpleRouter()
router.register(r'emails', ProvideEmailViewSet, base_name='emails')

# URLs
urlpatterns = [
    url(r'^', include(router.urls)),
]
