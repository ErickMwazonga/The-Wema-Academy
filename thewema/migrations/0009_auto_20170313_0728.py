# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-13 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thewema', '0008_auto_20170313_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclass',
            name='year',
            field=models.DateField(help_text='Use this format : YYYY-MM-DD'),
        ),
    ]
