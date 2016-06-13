from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Latlan(models.Model):
    lat = models.FloatField()
    lan = models.FloatField()
    updatedat = models.DateTimeField(default=timezone.now())

