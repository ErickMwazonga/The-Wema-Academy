# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 23:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thewema', '0022_auto_20170329_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='score',
            new_name='marks',
        ),
    ]