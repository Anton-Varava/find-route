from django.urls import path
from . import views

urlpatterns = [
    path('list', views.CityListView.as_view(), name='list-city'),
    path('add', views.CityCreateView.as_view(), name='add-city'),
    path('<int:pk>/edit', views.CityUpdateView.as_view(), name='update-city'),
    path('<int:pk>/delete', views.CityDeleteView.as_view(), name='delete-city')
]
