from django.contrib import admin
from .models import *
class CustomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)


# Register your models here.

admin.site.register(Libraries, CustomAdmin)
admin.site.register(Authors, CustomAdmin)
admin.site.register(Books, CustomAdmin)

