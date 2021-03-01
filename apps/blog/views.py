from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.blog.models import Blog, Category, Tag
from apps.setting.models import SEO, SocialSettings, Address, Logo, Title

class BlogList(ListView):
    model = Blog
    ordering =['-created_at']
    context_object_name = 'list_blogs'
    template_name = 'blog.html'
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context["seo"] = SEO.objects.all().first()
        context["blogs"] = Blog.objects.filter().order_by('-count')[:2]
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context

class BlogDetail(DetailView):
    model = Blog
    
    template_name='single-blog.html'
    context_object_name='single_blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        context['categories']= Category.objects.all()
        context["blogs"] = Blog.objects.filter().order_by('-count')[:2]
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        self.object.save()
        return context

class CategoryBlogListView(ListView):
    model = Blog
    template_name = 'blog-by-category.html'
    context_object_name = 'list_blogs'
    ordering =['-created_at']

    def get_queryset(self):
        return Blog.objects.filter(category=self.kwargs.get('category')).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        context['categories']= Category.objects.all()
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        context["blogs"] = Blog.objects.filter().order_by('-count')[:2]
        return context