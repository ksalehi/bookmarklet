from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Version(models.Model):
    major = models.PositiveSmallIntegerField(default=0)
    minor = models.PositiveSmallIntegerField(default=0)
    patch = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('major', 'minor', 'patch')

    def __unicode__(self):
        return "%d.%d.%d" % (self.major, self.minor, self.patch)