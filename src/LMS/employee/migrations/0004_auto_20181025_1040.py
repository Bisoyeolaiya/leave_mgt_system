# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20181024_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email_add',
            field=models.CharField(max_length=100, verbose_name='Email address'),
        ),
    ]
