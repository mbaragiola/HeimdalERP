# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('client_type', models.CharField(choices=[('C', 'Company'), ('I', 'Individual')], max_length=1, verbose_name='client type')),
                ('born_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country', verbose_name='born in')),
                ('extra_emails', models.ManyToManyField(blank=True, to='persons.ExtraEmailAddress', verbose_name='extra email addresses')),
            ],
            options={
                'verbose_name_plural': 'clients',
                'verbose_name': 'client',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='CompanyInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.ManyToManyField(blank=True, related_name='companies', related_query_name='company', to='invoice.Client', verbose_name='clients')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persons.Company')),
            ],
            options={
                'verbose_name_plural': 'companies',
                'verbose_name': 'company',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='FiscalPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'fiscal positions',
                'verbose_name': 'fiscal position',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(verbose_name='number')),
                ('invoice_date', models.DateField(help_text='Not necessarily today.', verbose_name='date')),
                ('invoice_status', models.CharField(choices=[('D', 'Draft'), ('S', 'Sent'), ('P', 'Paid'), ('C', 'Canceled')], default='D', max_length=1, verbose_name='status')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, help_text='Total without taxes.', max_digits=12, verbose_name='subtotal')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, help_text='Subtotal plus taxes.', max_digits=12, verbose_name='total')),
                ('notes', models.TextField(blank=True, default='', verbose_name='notes')),
                ('clients', models.ManyToManyField(related_name='invoices', related_query_name='invoice', to='invoice.Client', verbose_name='clients')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', related_query_name='invoice', to='persons.Company', verbose_name='company')),
            ],
            options={
                'verbose_name_plural': 'invoices',
                'verbose_name': 'invoice',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price_override', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='product price')),
                ('product_discount', models.FloatField(blank=True, default=0.0, help_text='A number between 0.00 and 1.00', verbose_name='product discount')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
            ],
            options={
                'verbose_name_plural': 'invoice lines',
                'verbose_name': 'invoice line',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='It could also be a service.', max_length=150, verbose_name='name')),
                ('suggested_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='suggested price')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='product', to='persons.Company', verbose_name='company')),
            ],
            options={
                'verbose_name_plural': 'products',
                'verbose_name': 'product',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='VAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='i.e. 8%', max_length=15, unique=True, verbose_name='name')),
                ('tax', models.FloatField(help_text='A value between 0.00 and 1.00', verbose_name='tax')),
            ],
            options={
                'verbose_name_plural': 'VATs',
                'verbose_name': 'VAT',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.AddField(
            model_name='invoiceproduct',
            name='vat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='product', to='invoice.VAT', verbose_name='VAT'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_lines', related_query_name='invoice_line', to='invoice.InvoiceProduct', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='product_vat_override',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_lines', related_query_name='invoice_line', to='invoice.VAT', verbose_name='VAT override'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_lines',
            field=models.ManyToManyField(related_name='invoices', related_query_name='invoice', to='invoice.InvoiceLine', verbose_name='invoice lines'),
        ),
        migrations.AddField(
            model_name='companyinvoice',
            name='fiscal_position',
            field=models.ForeignKey(blank=True, help_text='Certain countries require a fiscal position for its taxpayers.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', related_query_name='company', to='invoice.FiscalPosition', verbose_name='fiscal position'),
        ),
        migrations.AddField(
            model_name='client',
            name='fiscal_position',
            field=models.ForeignKey(blank=True, help_text='Certain countries require a fiscal position for its taxpayers.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', related_query_name='client', to='invoice.FiscalPosition', verbose_name='fiscal position'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone_numbers',
            field=models.ManyToManyField(blank=True, to='persons.PhoneNumber', verbose_name='phone numbers'),
        ),
        migrations.AlterUniqueTogether(
            name='invoiceproduct',
            unique_together=set([('company', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='invoiceproduct',
            index_together=set([('company', 'name')]),
        ),
    ]