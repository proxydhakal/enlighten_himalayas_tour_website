from django.shortcuts import render
from django.conf import settings
from django.core.mail import  send_mail
from django.views.generic import TemplateView
from apps.blog.models import Blog
from apps.country.models import Country
from apps.core.models import Slider,About, Service, Review
from apps.setting.models import SEO, SocialSettings, Address, Logo, Title

class IndexView(TemplateView):
    model = Slider
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Slider.objects.all()
        context["blogs"] = Blog.objects.filter().order_by('-created_at')[:3]
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["services"] = Service.objects.all()
        context["reviews"] = Review.objects.all()
        context["countries"] = Country.objects.filter().order_by('created_at')[:3]
        context["social"] = SocialSettings.objects.all().first()
        return context

class AboutView(TemplateView):
    model = About
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        context["about"] = About.objects.all().first()
        context["services"] = Service.objects.all()
        context["reviews"] = Review.objects.all()
        context["blogs"] = Blog.objects.filter().order_by('-created_at')[:3]
        return context


def contact(request):
    title = Title.objects.all().first()
    logo = Logo.objects.all().first()
    address = Address.objects.all().first()
    social = SocialSettings.objects.all().first()
    context = {'title':title, 'logo':logo ,'address': address, 'social': social}
    template_name='contact.html'
    if request.method == 'POST':
            message = request.POST['message']
            subject = request.POST['subject']
            email = request.POST['email']
            send_mail(subject,
            message, 
            email,
            ['shekhardhakal2015@gmail.com'], 
            fail_silently=False)
    return render(request, template_name, context)