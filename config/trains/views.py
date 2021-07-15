from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Train
from .forms import TrainCreateForm


# Create your views here.
class TrainListView(ListView):
    model = Train
    paginate_by = 10
    context_object_name = 'trains'
    ordering = ['number']


class TrainCreateView(CreateView):
    model = Train
    form_class = TrainCreateForm
    success_message = 'Train created successfully'
    success_url = 'list'
