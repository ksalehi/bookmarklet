from __future__ import absolute_import

from django.conf.urls import url, include

urlpatterns = [
   url(r'^discovery/', include('discovery.api.urls')),
]