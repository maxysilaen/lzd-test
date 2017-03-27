from django.shortcuts import render
from charts.models import (Penjualan, StatusItemPenjualan,
	ItemPenjualan)
# Create your views here.

def migrate_penjualan(request):
	object_list = Penjualan.objects.using('lazada').all()
	for obj in object_list:
		new_obj = Penjualan()
		new_obj.id_penjualan  = obj.id_penjualan
		new_obj.nama_customer = obj.nama_customer
		new_obj.email_customer = obj.email_customer 
		new_obj.nomor_order = obj.nomor_order  
		new_obj.total_harga = obj.total_harga
		new_obj.total_pajak = obj.total_pajak 
		new_obj.kode_kupon = obj.kode_kupon 
		new_obj.created_at = obj.created_at
		new_obj.updated_at = obj.updated_at
		new_obj.save(using='default')
		print(new_obj.id_penjualan)

def migrate_statusitempenjualan(request):
	object_list = StatusItemPenjualan.objects.using('lazada').all()
	for obj in object_list:
		new_obj = StatusItemPenjualan()
		new_obj.id_status_item_penjualan = obj.id_status_item_penjualan 
		new_obj.keterangan = obj.keterangan 
		new_obj.save(using='default')

def migrate_itempenjualan(request):
	object_list = ItemPenjualan.objects.using('lazada').all()
	for obj in object_list:
		try:
			get_penjualan = Penjualan.objects.get(id_penjualan=obj.fk_penjualan.id_penjualan)
			get_status_penjualan = StatusItemPenjualan.objects.get(id_status_item_penjualan=obj.fk_status_item_penjualan.id_status_item_penjualan)
			
			new_obj = ItemPenjualan()
			new_obj.id_item_penjualan = obj.id_item_penjualan
			new_obj.fk_penjualan = get_penjualan
			new_obj.fk_status_item_penjualan = get_status_penjualan
			new_obj.harga_satuan = obj.harga_satuan
			new_obj.jumlah_bayar = obj.jumlah_bayar
			new_obj.nilai_kupon = obj.nilai_kupon
			new_obj.persentase_kupon = obj.persentase_kupon
			new_obj.nama_produk = obj.nama_produk
			new_obj.kode_produk = obj.kode_produk
			new_obj.created_at = obj.created_at
			new_obj.updated_at = obj.updated_at
			new_obj.jumlah_diskon_cart_rule = obj.jumlah_diskon_cart_rule
			new_obj.kode_cart_rule = obj.kode_cart_rule
			obj.save(using='default')
		except Penjualan.DoesNotExist:
			pass
		print(obj.id_item_penjualan)