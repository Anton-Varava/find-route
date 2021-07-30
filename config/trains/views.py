from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Train
from .forms import TrainCreateForm


# Create your views here.
class TrainListView(ListView):
    model = Train
    paginate_by = 15
    context_object_name = 'trains'
    ordering = ['number']


class TrainCreateView(CreateView):
    model = Train
    form_class = TrainCreateForm
    success_message = 'Train created successfully'
    success_url = reverse_lazy('trains:list-train')


class TrainDeleteView(DeleteView):
    model = Train
    success_message = 'Train deleted successfully'
    success_url = reverse_lazy('trains:list-train')


class TrainUpdateView(UpdateView):
    model = Train
    success_url = reverse_lazy('trains:list-train')
    fields = '__all__'
    


