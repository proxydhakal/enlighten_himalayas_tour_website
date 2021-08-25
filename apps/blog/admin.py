from django.contrib import admin
from apps.blog.models import Blog,Category,Tag
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
from image_cropping import ImageCroppingMixin



class BlogAdmin(ImageCroppingMixin,admin.ModelAdmin):
    list_filter = ['category']
    search_fields = ['title']




admin.site.register(Blog, BlogAdmin)