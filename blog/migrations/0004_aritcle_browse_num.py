# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170502_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='aritcle',
            name='browse_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
