 
from django.urls import path
from apps.core import views
from apps.core.views import IndexView,AboutView,ContactCreateView

urlpatterns = [
    
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('newsletter/', views.subscribe_to_newsletter, name="subscribe"),
]