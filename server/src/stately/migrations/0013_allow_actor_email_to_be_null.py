# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stately', '0012_rename_case_state_to_currentstate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]