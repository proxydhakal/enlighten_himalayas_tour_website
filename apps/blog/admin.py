from django.contrib import admin
from apps.blog.models import Blog,Category,Tag
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)




class BlogAdmin(admin.ModelAdmin):
    list_filter = ['category']
    search_fields = ['title']
    list_display=('title','image_tag')




admin.site.register(Blog, BlogAdmin)