# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-13 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thewema', '0007_auto_20170312_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(help_text='Use this format : YYYY-MM-DD'),
        ),
    ]
