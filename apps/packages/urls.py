from django.urls import path
from apps.country.views import CountryView, CountryDetail
from apps.packages.views import PackageDetailView

urlpatterns = [
    path('<str:slug>', PackageDetailView.as_view(), name='packagedetail'),

]