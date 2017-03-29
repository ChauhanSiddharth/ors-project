# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-29 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule_Master',
            fields=[
                ('Schedule_master_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Schedule_datetime', models.DateTimeField()),
                ('Schedule_description', models.CharField(max_length=255)),
                ('Schedule_title', models.CharField(max_length=20)),
                ('Class_held_status', models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete'), ('Cancelled', 'Cancelled')], max_length=20)),
                ('Extra_notes', models.CharField(max_length=255)),
                ('Status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], max_length=20)),
                ('Class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_details.Class_Master')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule_Syllabus',
            fields=[
                ('Schedule_syllabus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Session_type', models.CharField(choices=[('Regular', 'Regular'), ('Extra', 'Extra')], max_length=20)),
                ('Extra_notes', models.CharField(max_length=255)),
                ('Schedule_master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Schedule_Master')),
            ],
        ),
    ]
