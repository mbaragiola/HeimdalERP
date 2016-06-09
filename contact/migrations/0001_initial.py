# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('phone_numbers', models.CharField(blank=True, default='', max_length=300, verbose_name='phone numbers')),
                ('extra_emails', models.CharField(blank=True, default='', max_length=300, verbose_name='extra email addresses')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('contact_type', models.CharField(choices=[('C', 'Company'), ('I', 'Individual')], max_length=1, verbose_name='contact type')),
                ('born_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country', to_field='geoname_id', verbose_name='born in')),
                ('home_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='persons.PhysicalAddress', verbose_name='home address')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
    ]
