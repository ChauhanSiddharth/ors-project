# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='files',
            field=models.FileField(upload_to=b''),
        ),
    ]
