# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-26 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thewema', '0017_auto_20170326_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='thewema.Subject'),
            preserve_default=False,
        ),
    ]
