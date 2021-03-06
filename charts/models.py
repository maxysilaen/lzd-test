# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q

class Penjualan(models.Model):
    id_penjualan = models.AutoField(primary_key=True)
    nama_customer = models.CharField(max_length=255, blank=True, null=True)
    email_customer = models.CharField(max_length=255)
    nomor_order = models.CharField(unique=True, max_length=45, blank=True, null=True)
    total_harga = models.DecimalField(max_digits=17, decimal_places=2)
    total_pajak = models.DecimalField(max_digits=17, decimal_places=2)
    kode_kupon = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        
        db_table = 'penjualan'


class StatusItemPenjualan(models.Model):
    id_status_item_penjualan = models.AutoField(primary_key=True)
    keterangan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'status_item_penjualan'

    def __str__(self): #def __str__(self):
        return self.keterangan
class ItemPenjualanQuerySet(models.query.QuerySet):
    def stat27(self):
        return self.filter(fk_status_item_penjualan=27)
    def stat71(self):
        return self.filter(fk_status_item_penjualan=71)
    def stat75(self):
        return self.filter(fk_status_item_penjualan=75)
    def stat76(self):
        return self.filter(fk_status_item_penjualan=76)
    def stat81(self):
        return self.filter(fk_status_item_penjualan=81)
    def stat84(self):
        return self.filter(fk_status_item_penjualan=84)
    def stat86(self):
        return self.filter(fk_status_item_penjualan=86)

class ItemPenjualanManager(models.Manager):
    def get_queryset(self):
        return ItemPenjualanQuerySet(self.model, using=self._db)

    def get_stat27(self, *args, **kwargs):
        return self.get_queryset().stat27()
    def get_stat71(self, *args, **kwargs):
        return self.get_queryset().stat71()
    def get_stat75(self, *args, **kwargs):
        return self.get_queryset().stat75()
    def get_stat76(self, *args, **kwargs):
        return self.get_queryset().stat76()
    def get_stat81(self, *args, **kwargs):
        return self.get_queryset().stat81()
    def get_stat84(self, *args, **kwargs):
        return self.get_queryset().stat84()
    def get_stat86(self, *args, **kwargs):
        return self.get_queryset().stat86()


class ItemPenjualan(models.Model):
    id_item_penjualan = models.AutoField(primary_key=True)
    fk_penjualan = models.ForeignKey(Penjualan, blank=True, null=True,
        db_column="fk_penjualan", db_index=True)
    fk_status_item_penjualan = models.ForeignKey(StatusItemPenjualan, 
        blank=True, null=True, db_column="fk_status_item_penjualan", db_index=True)
    harga_satuan = models.DecimalField(max_digits=17, decimal_places=2)
    jumlah_bayar = models.DecimalField(max_digits=17, decimal_places=2)
    nilai_kupon = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    persentase_kupon = models.IntegerField(blank=True, null=True)
    nama_produk = models.CharField(max_length=255)
    kode_produk = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    jumlah_diskon_cart_rule = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    kode_cart_rule = models.TextField(blank=True, null=True)
    objects = ItemPenjualanManager()
    class Meta:
        
        db_table = 'item_penjualan'

    def __str__(self): #def __str__(self):
        return self.nama_produk 