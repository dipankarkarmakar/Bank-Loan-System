# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.CharField(max_length=255)),
                ('ifsc', models.CharField(max_length=255)),
            ],
        ),
    ]
