from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import City
from .forms import CityCreateForm


# Create your views here.
class CityListView(ListView):
    model = City
    paginate_by = 10
    context_object_name = 'cities'
    ordering = ['title']


class CityCreateView(CreateView):
    model = City
    form_class = CityCreateForm
    success_message = 'City created successfully'
    success_url = reverse_lazy('cities:list-city')


class CityDeleteView(DeleteView):
    model = City
    success_url = reverse_lazy('cities:list-city')
    success_message = 'City deleted successfully'


class CityUpdateView(UpdateView):
    model = City
    success_url = reverse_lazy('cities:list-city')
    fields = ['title']
