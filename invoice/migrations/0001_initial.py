# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 11:22
from __future__ import unicode_literals

import common.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
        ('contact', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(max_length=300, verbose_name='legal name')),
                ('initiated_activities', models.DateField(blank=True, null=True, validators=[common.validators.date_is_present_or_past], verbose_name='initiated activities')),
                ('default_invoice_credit_account', models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default invoice credit account')),
                ('default_invoice_debit_account', models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default invoice debit account')),
                ('fiscal_address', models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='persons.PhysicalAddress', verbose_name='fiscal address')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'companies',
                'verbose_name': 'company',
            },
        ),
        migrations.CreateModel(
            name='ContactInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(max_length=300, verbose_name='legal name')),
                ('contact_contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact', verbose_name='contact')),
                ('fiscal_address', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='persons.PhysicalAddress', verbose_name='fiscal address')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'contacts',
                'verbose_name': 'contact',
            },
        ),
        migrations.CreateModel(
            name='FiscalPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('code', models.SlugField(blank=True, default='', help_text='Some local official electronic systems handle specific codes.', max_length=15, verbose_name='code')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'fiscal positions',
                'verbose_name': 'fiscal position',
            },
        ),
        migrations.CreateModel(
            name='FiscalPositionHasInvoiceTypeAllowed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiscal_position_issuer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='invoice.FiscalPosition', verbose_name='fiscal position issuer')),
                ('fiscal_position_receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='invoice.FiscalPosition', verbose_name='fiscal position receiver')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'fiscal positions have invoice types allowed',
                'verbose_name': 'fiscal position has invoice type allowed',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.BigIntegerField(blank=True, default=0, verbose_name='number')),
                ('invoice_date', models.DateField(help_text='Not necessarily today.', validators=[common.validators.date_is_present_or_past], verbose_name='date')),
                ('status', models.CharField(choices=[('D', 'Draft'), ('A', 'Accepted'), ('T', 'Authorized'), ('C', 'Canceled')], default='D', max_length=1, verbose_name='status')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, help_text='Total without taxes.', max_digits=12, verbose_name='subtotal')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, help_text='Subtotal plus taxes.', max_digits=12, verbose_name='total')),
                ('notes', models.TextField(blank=True, default='', verbose_name='notes')),
                ('invoice_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', related_query_name='invoice', to='invoice.CompanyInvoice', verbose_name='company')),
                ('invoice_contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', related_query_name='invoice', to='invoice.ContactInvoice', verbose_name='contact')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'invoices',
                'verbose_name': 'invoice',
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price_sold', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='price sold')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='A number between 0.00 and 1.00', max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='discount')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('description', models.CharField(blank=True, default='', max_length=300, verbose_name='description')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'invoice lines',
                'verbose_name': 'invoice line',
            },
        ),
        migrations.CreateModel(
            name='InvoiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('invoice_type_class', models.CharField(choices=[('B', 'Bill'), ('D', 'Debit'), ('C', 'Credit')], max_length=1, verbose_name='invoice type class')),
                ('code', models.SlugField(blank=True, default='', help_text='Some local official electronic systems handle specific codes.', max_length=15, verbose_name='code')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'invoice types',
                'verbose_name': 'invoice type',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='It could also be a service.', max_length=150, verbose_name='name')),
                ('current_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='current price')),
                ('invoice_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', related_query_name='product', to='invoice.CompanyInvoice', verbose_name='company')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'products',
                'verbose_name': 'product',
            },
        ),
        migrations.CreateModel(
            name='VAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='i.e. 8% US', max_length=15, unique=True, verbose_name='name')),
                ('code', models.SlugField(blank=True, default='', help_text='Some local official electronic systems handle specific codes.', max_length=15, verbose_name='code')),
                ('tax', models.DecimalField(decimal_places=2, help_text='A value between 0.00 and 1.00', max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='tax')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'VATs',
                'verbose_name': 'VAT',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='vat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', related_query_name='product', to='invoice.VAT', verbose_name='VAT'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='product',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.PROTECT, related_name='invoice_lines', related_query_name='invoice_line', to='invoice.Product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_lines',
            field=models.ManyToManyField(blank=True, related_name='_invoice_invoice_lines_+', related_query_name='invoice', to='invoice.InvoiceLine', verbose_name='invoice lines'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='invoices', related_query_name='invoice', to='invoice.InvoiceType', verbose_name='invoice type'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='related_invoice',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='invoice.Invoice', verbose_name='related invoice'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='transaction',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='invoice', to='accounting.Transaction', verbose_name='transaction'),
        ),
        migrations.AddField(
            model_name='fiscalpositionhasinvoicetypeallowed',
            name='invoice_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='invoice.InvoiceType', verbose_name='invoice type'),
        ),
        migrations.AddField(
            model_name='contactinvoice',
            name='fiscal_position',
            field=models.ForeignKey(db_index=False, help_text='Certain countries require a fiscal position for its taxpayers.', on_delete=django.db.models.deletion.PROTECT, related_name='contacts', related_query_name='contact', to='invoice.FiscalPosition', verbose_name='fiscal position'),
        ),
        migrations.AddField(
            model_name='companyinvoice',
            name='fiscal_position',
            field=models.ForeignKey(blank=True, db_index=False, help_text='Certain countries require a fiscal position for its taxpayers.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='companies', related_query_name='company', to='invoice.FiscalPosition', verbose_name='fiscal position'),
        ),
        migrations.AddField(
            model_name='companyinvoice',
            name='persons_company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persons.Company', verbose_name='company'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('invoice_company', 'name')]),
        ),
    ]
