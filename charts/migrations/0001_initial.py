# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPenjualan',
            fields=[
                ('id_item_penjualan', models.AutoField(primary_key=True, serialize=False)),
                ('harga_satuan', models.DecimalField(decimal_places=2, max_digits=17)),
                ('jumlah_bayar', models.DecimalField(decimal_places=2, max_digits=17)),
                ('nilai_kupon', models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True)),
                ('persentase_kupon', models.IntegerField(blank=True, null=True)),
                ('nama_produk', models.CharField(max_length=255)),
                ('kode_produk', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField()),
                ('jumlah_diskon_cart_rule', models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True)),
                ('kode_cart_rule', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'item_penjualan',
            },
        ),
        migrations.CreateModel(
            name='Penjualan',
            fields=[
                ('id_penjualan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_customer', models.CharField(blank=True, max_length=255, null=True)),
                ('email_customer', models.CharField(max_length=255)),
                ('nomor_order', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('total_harga', models.DecimalField(decimal_places=2, max_digits=17)),
                ('total_pajak', models.DecimalField(decimal_places=2, max_digits=17)),
                ('kode_kupon', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'penjualan',
            },
        ),
        migrations.CreateModel(
            name='StatusItemPenjualan',
            fields=[
                ('id_status_item_penjualan', models.AutoField(primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'status_item_penjualan',
            },
        ),
        migrations.AddField(
            model_name='itempenjualan',
            name='fk_penjualan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='charts.Penjualan'),
        ),
        migrations.AddField(
            model_name='itempenjualan',
            name='fk_status_item_penjualan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='charts.StatusItemPenjualan'),
        ),
    ]
