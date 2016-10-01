# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='defloration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
