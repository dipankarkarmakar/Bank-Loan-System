# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_accountdetails_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetails',
            name='account_number',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
