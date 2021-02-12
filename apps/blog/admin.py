from django.contrib import admin
from apps.blog.models import Blog,Category,Tag
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)

