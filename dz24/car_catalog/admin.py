from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['preview', 'links']



    def preview(self,obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 200px;">')

    def links(self, obj):
        return mark_safe(f'<a href="{obj.link}">link<a>')

admin.site.register(Car, PostAdmin)
admin.site.register(OptionalEquipment)