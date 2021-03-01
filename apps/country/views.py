from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from apps.country.models import Country, Destinations
from apps.blog.models import Blog
from apps.core.models import Slider, Service, Review
from apps.setting.models import SEO, SocialSettings, Address, Logo, Title
from apps.activities.models import Activity

class CountryView(TemplateView):
    model = Country
    template_name = "destination.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Slider.objects.all()
        context["countries"] = Country.objects.all()
        context["blogs"] = Blog.objects.filter().order_by('-created_at')[:3]
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["destination"] = Destinations.objects.all().first()
        context["services"] = Service.objects.all()
        context["reviews"] = Review.objects.all()
        context["social"] = SocialSettings.objects.all().first()
        return context


class CountryDetail(DetailView):
    model = Country  
    template_name='activity.html'
    context_object_name='single_country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.filter().order_by('-created_at')[:3]
        context["activities"] = Activity.objects.filter(country=1)
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context