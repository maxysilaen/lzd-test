from django.conf.urls import url
from migrationdb.views import migrate_penjualan, migrate_itempenjualan

urlpatterns = [

    
    url(r'^penjualan/$', migrate_penjualan, name='penjualan'),
    url(r'^item-penjualan/$', migrate_itempenjualan, name='item-penjualan'),
   

]

