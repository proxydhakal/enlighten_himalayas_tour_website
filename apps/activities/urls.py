from django.urls import path
from apps.activities.views import ActivityDetail

urlpatterns = [

    path('<str:slug>/', ActivityDetail.as_view(), name='activity'),
]