from django.urls import path
from apps.country.views import CountryView, CountryDetail
from apps.activities.views import ActivityDetail

urlpatterns = [
    path('', CountryView.as_view(), name='country'),
    path('<str:slug>/', CountryDetail.as_view(), name='countrydetail'),
    path('<str:slug>/', ActivityDetail.as_view(), name='activity'),
]