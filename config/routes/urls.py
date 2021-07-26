from django.urls import path
from .views import home, find_routes

urlpatterns = [
    path('', home, name='home'),
    path('find-routes/', find_routes, name='find-routes')
]