# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-14 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20190713_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='weight',
            field=models.IntegerField(default=1),
        ),
    ]
