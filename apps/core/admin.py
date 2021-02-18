from django.contrib import admin
from apps.core.models import Slider,About, Service, Review
from solo.admin import SingletonModelAdmin

admin.site.register(About, SingletonModelAdmin)
admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Review)


