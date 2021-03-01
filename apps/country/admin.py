from django.contrib import admin
from apps.country.models import Country,Destinations
from solo.admin import SingletonModelAdmin

admin.site.register(Destinations, SingletonModelAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Country, CountryAdmin)
