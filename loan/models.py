# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from bank.models import Bankdetails
from person.models import Persondetails
# Create your models here.


class Loandetails(models.Model):
    loan_amount = models.IntegerField(blank=True,null=True)
    interest_rate= models.DecimalField(max_digits=10,decimal_places=3)
    interest_amount = models.DecimalField(max_digits=10,decimal_places=3)
    repayment_amount = models.DecimalField(max_digits=10,decimal_places=3)
    loan_status = models.CharField(max_length=255)
    tenure = models.IntegerField()
    bank = models.ForeignKey(Bankdetails)
    person = models.ForeignKey(Persondetails)
