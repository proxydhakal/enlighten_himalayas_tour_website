from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from apps.country.models import Country, Destinations
from apps.blog.models import Blog
from apps.core.models import Slider, Service, Review
from apps.setting.models import SEO, SocialSettings, Address, Logo, Title
from apps.activities.models import Activity
from apps.country.models import Country
from apps.packages.models import Package

class PackageDetailView(DetailView):
    model = Package
    template_name = "package_detail.html"
    context_object_name = 'packages_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.kwargs.get('slug')
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
