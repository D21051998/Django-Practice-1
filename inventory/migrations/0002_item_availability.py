# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='availability',
            field=models.IntegerField(default=0),
        ),
    ]
