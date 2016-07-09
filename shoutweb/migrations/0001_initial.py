# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('hq_city', models.CharField(max_length=50)),
                ('hq_state', models.CharField(max_length=2)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]
