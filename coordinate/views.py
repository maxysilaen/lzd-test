from math import sqrt
from django.shortcuts import render
from django.views.generic import View

from .models import Coordinate

class CoordinateView(View):
	template_name = "coordinate/sorting_results.html"
	list_distance = []

	def calculate_distance(self, coordinate1, coordinate2):
		#return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)
		return sqrt( ((coordinate1[0]-coordinate2[0])**2) + ((coordinate1[1]-coordinate2[1])**2) )

	def get(self, request, *args, **kwargs):
		
		points = Coordinate.objects.values_list('point_x','point_y')
		print(points)
		len_object = len(points)
		distances = []
		logs = []
		for i in range(len_object-1):
		    for j in range(i+1, len_object):
		        distances.append(self.calculate_distance(points[i],points[j]))
		        logs.append(tuple((i, j)))
		
		
		min_index = (distances.index(min(distances)))
		logs_min_index = logs[min_index]
		index_coordinate1 = logs_min_index[0]
		index_coordinate2 = logs_min_index[1]
		coordinate1 = points[index_coordinate1]
		coordinate2 = points[index_coordinate2]
		
		context = {
		'object_list' : points,
		'len_object' : len_object,
		'shortest_distance': min(distances), 
		'coordinate1':coordinate1,
		'coordinate2':coordinate2,
		}
		template = self.template_name
		return render(request, template, context)