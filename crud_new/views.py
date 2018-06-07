from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from crud.models import *
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'crud/home.html'


class MembreCreateView(CreateView):
    model = Membre
    fields = ('civilite', 'nom', 'prenom', 'date_de_naissance')
    success_url = reverse_lazy('membre_list')
    template_name = 'crud/membre_create.html'


class MembreDetailView(DetailView):
    model = Membre
    success_url = reverse_lazy('membre_list')
    template_name = 'crud/membre_detail.html'


class MembreUpdateView(UpdateView):
    model = Membre
    success_url = reverse_lazy('membre_list')
    template_name = 'crud/membre_update.html'


class MembreDeleteView(DeleteView):
    model = Membre
    template_name = 'crud/membre_delete.html'
    success_url = reverse_lazy('membre_list')


class MembreListView(ListView):
    model = Membre
    fields = ('civilite', 'nom', 'prenom', 'date_de_naissance')
    template_name = 'crud/membre_list.html'




