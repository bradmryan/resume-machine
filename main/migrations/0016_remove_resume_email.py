# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 04:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_resume_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
    ]
