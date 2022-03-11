from django.contrib import admin
from apps.core.models import Slider,About, Service, Review,Contact,Newsletter
from solo.admin import SingletonModelAdmin

admin.site.register(About, SingletonModelAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(Slider, SliderAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
    
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review)
admin.site.register(Newsletter)

class SomeAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')
    def changelist_view(self, request, extra_context=None):
        self.list_display_links = (None, )
        return super(SomeAdmin, self).changelist_view(request, extra_context=None)
admin.site.register(Contact,SomeAdmin)


