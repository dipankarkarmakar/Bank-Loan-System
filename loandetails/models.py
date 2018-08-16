# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from loan.models import Loandetails

from person.models import Persondetails


class Loandata(models.Model):
    payable_date = models.DateField()
    payable_amount = models.IntegerField()
    payable_status = models.CharField(max_length=255)
    loan = models.ForeignKey(Loandetails)
    person = models.ForeignKey(Persondetails)
