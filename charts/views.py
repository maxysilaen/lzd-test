import datetime 
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Penjualan, ItemPenjualan, StatusItemPenjualan
from .forms import FilterStatusForm


# Create your views here.

class HomeView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["title"] = "Lazada Test"
		return context
class HomeChartView(View):
	def get(self, request, *args, **kwargs):
		date = request.GET.get('date')
		if date == None:
			date = "2017-02-01"
		context = {
		'date':date,
		}
		print(date)
		return render(request, 'charts.html', context)

class ChartDataAPI(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		query = request.GET.get("date")
		if query:
			date=request.GET.get("date")
		elif query is None:
			date=datetime.date.today()	
		count_stat27 = ItemPenjualan.objects.get_stat27().filter(updated_at__date=date).count()
		count_stat71 = ItemPenjualan.objects.get_stat71().filter(updated_at__date=date).count()
		count_stat75 = ItemPenjualan.objects.get_stat75().filter(updated_at__date=date).count()
		count_stat76 = ItemPenjualan.objects.get_stat76().filter(updated_at__date=date).count()
		count_stat81 = ItemPenjualan.objects.get_stat81().filter(updated_at__date=date).count()
		count_stat84 = ItemPenjualan.objects.get_stat84().filter(updated_at__date=date).count()
		count_stat86 = ItemPenjualan.objects.get_stat86().filter(updated_at__date=date).count()
		


		labels = ["27", "71", "75", "76", "81", "84", "86"]
		default_items = [count_stat27, count_stat71, count_stat75, count_stat76, 
		count_stat81, count_stat84,count_stat86]
		data = {
				"default": default_items,
		        "labels": labels,
		       
		}
		return Response(data)
class PenjualanView(ListView):
	model=ItemPenjualan
	template_name="penjualan.html"
	queryset = ItemPenjualan.objects.all()
	paginate_by = 50

	def get_context_data(self, *args, **kwargs):
		context = super(PenjualanView, self).get_context_data(*args, **kwargs)
		context["form"] = FilterStatusForm
		context["count"] = self.get_queryset().count()
		query = self.request.GET.get("status")
		if query==None:
			query="All"
		context["query"] = query
		
		return context

	
	def get_queryset(self, *args, **kwargs):
			qs = super(PenjualanView, self).get_queryset(*args, **kwargs)
			query = self.request.GET.get("status")
			print(query)
			if query == None or query=="All":
				return qs
			else:
				qs = self.model.objects.filter(
					Q(fk_status_item_penjualan__id_status_item_penjualan=query)
					)
				return qs