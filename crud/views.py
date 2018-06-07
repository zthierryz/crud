from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from crud.models import *
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'crud/home.html'


class MembreCreateView(CreateView):
    model = Membre
    fields = ('civilite', 'nom', 'prenom', 'date_de_naissance')
    success_url = reverse_lazy('home')
    template_name = 'crud/membre_create.html'


class MembreListView(ListView):
    model = Membre
    template_name = 'crud/membre_list.html'


class MembreDetailView(DetailView):
    model = Membre
    template_name = 'crud/membre_read.html'

    def get_succes_url(self):
    	if tagada:
    		return reverse_lazy('membre_delete')
    	else:
    		return reverse_lazy('membre_update')



class MembreUpdateView(UpdateView):
    pass


class MembreDeleteView(DeleteView):
    pass
