from django.urls import path
from apps.country.views import CountryView, CountryDetail

urlpatterns = [
    path('', CountryView.as_view(), name='country'),
    path('<str:slug>/', CountryDetail.as_view(), name='country'),
    

]