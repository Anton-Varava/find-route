from django.urls import path
from . import views

urlpatterns = [
    path('list', views.CityListView.as_view(), name='list-city'),
    path('add', views.CityCreateView.as_view(), name='add-city')
]