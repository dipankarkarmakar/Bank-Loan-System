# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_auto_20180313_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loandetails',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Bankdetails'),
        ),
        migrations.AlterField(
            model_name='loandetails',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Persondetails'),
        ),
    ]
