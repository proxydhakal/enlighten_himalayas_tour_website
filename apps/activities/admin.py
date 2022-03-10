from pyexpat import model
from django.contrib import admin
from apps.activities.models import  Activity
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    
    list_display=('title','image_tag')
admin.site.register(Activity, ActivityAdmin)