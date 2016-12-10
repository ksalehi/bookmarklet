"""
    API URLs for Internal
"""
from __future__ import absolute_import

from django.conf.urls import include, url
from rest_framework import routers

from .views import CountUsersView

# Routers
analytics_urls = [
    url(r'^count-users/', CountUsersView.as_view()),
]

# URLs
urlpatterns = [
    url(r'^analytics/', include(analytics_urls)),
]
