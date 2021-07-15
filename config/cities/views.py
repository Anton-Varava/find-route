from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django import forms

from .models import City
from .forms import CityCreateForm


# Create your views here.
class CityListView(ListView):
    model = City
    paginate_by = 10
    context_object_name = 'cities'
    ordering = ['title']
    # template_name = 'cities/city_list.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityCreateForm
    success_message = 'City created successfully'
    success_url = 'list'