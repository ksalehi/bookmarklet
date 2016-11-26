"""
    View URLs for Internal
"""
from __future__ import absolute_import

from django.conf.urls import include, url
from rest_framework import routers

from .views import analytics

# URLs
urlpatterns = [
    url(r'^analytics/', analytics, name='analytics'),
]
