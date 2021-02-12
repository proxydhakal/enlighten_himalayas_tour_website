from django.urls import path
from apps.blog.views import BlogList, BlogDetail, CategoryBlogListView

urlpatterns = [
    path('', BlogList.as_view(), name='blog'),
    path('<str:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('category/<str:category>', CategoryBlogListView.as_view(), name='blog-cat'),

]