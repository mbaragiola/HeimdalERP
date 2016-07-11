# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 14:26
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fantasy_name', models.CharField(max_length=150, verbose_name='fantasy name')),
                ('legal_name', models.CharField(blank=True, default='', max_length=300, verbose_name='legal name')),
                ('slogan', models.CharField(blank=True, default='', max_length=200, verbose_name='slogan')),
                ('initiated_activities', models.DateField(blank=True, null=True, validators=[common.validators.date_is_present_or_past], verbose_name='initiated activities')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='PhysicalAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, default='', max_length=150, verbose_name='street address')),
                ('floor_number', models.CharField(blank=True, default='', max_length=4, verbose_name='floor number')),
                ('apartment_number', models.CharField(blank=True, default='', max_length=6, verbose_name='apartment number')),
                ('postal_code', models.CharField(blank=True, default='', max_length=20, verbose_name='postal code')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='physical_addresses', related_query_name='physical_address', to='geo.Locality', verbose_name='locality')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name': 'physical address',
                'verbose_name_plural': 'physical addresses',
            },
        ),
    ]
