from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Coordinate
# Register your models here.

class CoordinateResource(resources.ModelResource):

    class Meta:
        model = Coordinate
        fields = ('id','point_x', 'point_y')
        export_order = ('id','point_x', 'point_y')
        
class CoordinateAdmin(ImportExportModelAdmin):
	resource_class = CoordinateResource
	list_display = ['point_x','point_y',
	]
	list_display_links = ['point_x',]

	list_per_page = 15
admin.site.register(Coordinate, CoordinateAdmin)