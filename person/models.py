from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Persondetails(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    mobile_number = models.IntegerField(unique=True)
    city = models.CharField(max_length=255)
