# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_loandetails_tenure'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandetails',
            name='loan_status',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
