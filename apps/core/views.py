from django.shortcuts import render
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


# Create your views here.
def index(request):
    template_name='index.html'
    return render(request, template_name)

def about(request):
    template_name='about.html'
    return render(request, template_name)

# def blog(request):
#     template_name='blog.html'
#     return render(request, template_name)

def destination(request):
    template_name='destination.html'
    return render(request, template_name)

def contact(request):
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
    return render(request, template_name)