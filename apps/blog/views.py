from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.blog.models import Blog, Category, Tag


class BlogList(ListView):
    model = Blog
    ordering =['-created_at']
    context_object_name = 'list_blogs'
    template_name = 'blog.html'
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BlogDetail(DetailView):
    model = Blog
    
    template_name='single-blog.html'
    context_object_name='single_blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        context["blogs"] = Blog.objects.filter().order_by('-count')[:2]
        context['categories']= Category.objects.all()
        self.object.save()
        return context

class CategoryBlogListView(ListView):
    model =Blog
    template_name = 'blog_by_category.html'
    context_object_name = 'categories'
    ordering =['-created_at']

    def get_queryset(self):
        return Blog.objects.filter(category=self.kwargs.get('category')).order_by('-created_at')