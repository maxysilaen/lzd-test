from django.contrib import admin
from .models import Penjualan, StatusItemPenjualan, ItemPenjualan
# Register your models here.
admin.site.register(Penjualan)
admin.site.register(StatusItemPenjualan)
admin.site.register(ItemPenjualan)