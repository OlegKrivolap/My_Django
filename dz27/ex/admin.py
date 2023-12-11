from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class CarResources(resources.ModelResource):
    class Meta:
        model = Car
        fields = ('id', 'name' ,'color', 'photo', 'price')
        export_order = ('id', 'name' ,'color', 'price', 'photo')

class CarAdmin(ImportExportModelAdmin):
    resource_class = CarResources

admin.site.register(Car, CarAdmin)
