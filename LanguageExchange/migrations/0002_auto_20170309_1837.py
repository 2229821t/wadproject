# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LanguageExchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]