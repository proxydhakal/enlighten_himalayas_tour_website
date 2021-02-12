 
from django.urls import path
from apps.core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('destination/', views.destination, name='destination'),
    path('contact/', views.contact, name='contact'),
]