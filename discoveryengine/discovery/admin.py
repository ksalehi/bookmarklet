from __future__ import absolute_import

from django.contrib import admin

from .models import Question, Manuscript, Rating

# Register your models here.
admin.site.register(Question)
admin.site.register(Manuscript)
admin.site.register(Rating)