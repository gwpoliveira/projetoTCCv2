from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tcc
from .forms import TccForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
# class HomeTemplateView(TemplateView):
#     template_name = 'home.html'
    
#     def get_context_data(self, **kwargs):
        
#         context = super().get_context_data(**kwargs)
#         context['tcc'] = Tcc.objects.all()[:5]
        
#         return context

class TccListView(ListView):
    model = Tcc
    template_name = 'tcc/listar.html'
    context_object_name = 'tccs'
    ordering = '-id'

class TccDetailView(DetailView):
    model = Tcc
    template_name = 'tcc/detalhar.html'
    context_object_name = 'tcc'
    pk_url_kwarg = 'id'
    
class TccCreateView(CreateView):
    model = Tcc
    template_name = 'tcc/cadastrar.html'
    form_class = TccForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Tcc cadastrato com sucesso!")
        return reverse('listar-tcc')

class TccUpdateView(UpdateView):
    model = Tcc
    template_name = 'tcc/atualizar.html'
    form_class = TccForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Tcc atualizado com sucesso!")
        return reverse('listar-tcc')

class TccDeleteView(DeleteView):
    model = Tcc
    template_name = 'tcc/Ttc_confirm_delete.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Tcc deletado com sucesso!")
        return reverse('listar-tcc')