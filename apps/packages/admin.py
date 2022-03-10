from django.contrib import admin
from apps.packages.models import Package

class PackageAdmin(admin.ModelAdmin):
    list_filter = ['title']
    search_fields = ['title']
    list_display=('title','image_tag')


admin.site.register(Package, PackageAdmin)
