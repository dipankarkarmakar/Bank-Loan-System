# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20180314_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetails',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Bankdetails'),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Persondetails'),
        ),
    ]