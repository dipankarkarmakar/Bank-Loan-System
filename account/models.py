# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from bank.models import Bankdetails
from person.models import Persondetails

# Create your models here.
class Accountdetails(models.Model):
    holder_name = models.CharField(max_length=255,blank=True,null=True)
    account_type= models.CharField(max_length=255)
    account_number = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=10,decimal_places=3)
    bank = models.ForeignKey(Bankdetails)
    person = models.ForeignKey(Persondetails)
