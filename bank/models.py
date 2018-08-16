from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bankdetails(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    branch= models.CharField(max_length=255)
    ifsc = models.CharField(max_length=255)
