# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20171024_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsonsnippet',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=False, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=False, editable=False, unique=True),
        ),
    ]
