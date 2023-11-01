from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from birds.forms import BirdForm
from birds.models import Birds, ViewBirds


class BirdsListView(ListView):
    model = Birds
    template_name = 'birds/birds.html'


class BirdsCreateView(CreateView):
    model = Birds
    form_class = BirdForm
    success_url = reverse_lazy('birds:list')


class BirdsDetailView(DetailView):
    model = Birds


class BirdsUpdateView(UpdateView):
    model = Birds
    form_class = BirdForm
    success_url = reverse_lazy('birds:list')


class BirdsDeleteView(DeleteView):
    model = Birds
    fields = '__all__'
    success_url = reverse_lazy('birds:list')


def view_birds(request):
    context = {
        'object_list': Birds.objects.filter(vision_attribute=True),
    }
    return render(request, 'birds/view_birds.html', context)


class ViewBirdsListView(ListView):
    model = ViewBirds
    template_name = 'birds/view_birds.html'
