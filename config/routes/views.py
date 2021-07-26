from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RouteForm
from . import utils


# Create your views here.
def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            context = utils.get_context_for_routes_view(form)
            context['form'] = form
            return render(request, 'routes/home.html', context)
    else:
        form = RouteForm()
        return render(request, reverse_lazy('routes:home'), {'form': form})

