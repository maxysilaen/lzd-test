from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from charts.views import (ChartDataAPI, HomeChartView,
	PenjualanView, HomeView)

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^api/chart/$', ChartDataAPI.as_view(), name='chart_api'),
	url(r'^chart/', HomeChartView.as_view(), name='chart'),
	url(r'^penjualan/', PenjualanView.as_view(), name='penjualan'),
	url(r'^coordinate/', include('coordinate.urls', namespace='coordinate')),
	url(r'^migrate/', include('migrationdb.urls', namespace='migrate')),

  
]
if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    import debug_toolbar
    urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    