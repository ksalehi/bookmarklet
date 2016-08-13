from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import User
from django.db import models

from widget.models import Version

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    help_text = models.TextField()

    DISCOVERY_VALUE = "DV"
    ACTIONABILITY = "AC"
    CERTITUDE = "CR"
    EXPERTISE = "EX"
    CATEGORY_CHOICES = (
        (DISCOVERY_VALUE, "Discovery Value"),
        (ACTIONABILITY, "Actionability"),
        (CERTITUDE, "Certitude"),
        (EXPERTISE, "Expertise"),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DISCOVERY_VALUE
    )

    SLIDER = "SL"
    QUESTION_TYPE_CHOICES = (
        (SLIDER, "Slider"),
    )
    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE_CHOICES,
        default=SLIDER
    )

    def __unicode__(self):
        return "%s: %s" % (self.category, self.question_text)

class Manuscript(models.Model):
    doi = models.CharField(max_length=200)

    def __unicode__(self):
        return doi

class Rating(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    manuscript = models.ForeignKey(Manuscript)
    version = models.ForeignKey(Version)

    value = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s: %.2f" % (self.manuscript.doi, self.value)