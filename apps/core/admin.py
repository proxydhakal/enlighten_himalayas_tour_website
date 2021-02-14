from django.contrib import admin
from apps.core.models import Slider,About
# Register your models here.

from solo.admin import SingletonModelAdmin

admin.site.register(About, SingletonModelAdmin)

config = About.objects.get()
config = About.get_solo()
admin.site.register(Slider)


