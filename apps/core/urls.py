 
from django.urls import path
from apps.core import views
from apps.core.views import IndexView,AboutView

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('destination/', views.destination, name='destination'),
    path('contact/', views.contact, name='contact'),
]