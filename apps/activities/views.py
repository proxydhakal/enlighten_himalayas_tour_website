from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from apps.country.models import Country, Destinations
from apps.blog.models import Blog
from apps.core.models import Slider, Service, Review
from apps.setting.models import SEO, SocialSettings, Address, Logo, Title
from apps.activities.models import Activity
from apps.packages.models import Package



class ActivityDetail(DetailView):
    model = Activity  
    template_name='packages.html'
    context_object_name='single_activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.kwargs.get('slug')
        print(query)
        context["blogs"] = Blog.objects.filter().order_by('-created_at')[:3]
        context["packages"] = Package.objects.raw('''SELECT p.*, p.slug as p_slug , a.*
                                                    FROM activities_activity as a
                                                    INNER JOIN packages_package as p
                                                    ON p.activity_id=a.id
                                                    WHERE a.slug = %s;''',[query])
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context