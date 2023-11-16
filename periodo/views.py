from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Periodo
from .forms import PeriodoForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
# class HomeTemplateView(TemplateView):
#     template_name = 'home.html'
    
#     def get_context_data(self, **kwargs):
        
#         context = super().get_context_data(**kwargs)
#         context['periodo'] = Periodo.objects.all()[:5]
        
#         return context

class PeriodoListView(ListView):
    model = Periodo
    template_name = 'periodo/listar.html'
    context_object_name = 'periodos'
    ordering = '-periodo'

class PeriodoDetailView(DetailView):
    model = Periodo
    template_name = 'periodo/detalhar.html'
    context_object_name = 'periodo'
    pk_url_kwarg = 'id'
    
class PeriodoCreateView(CreateView):
    model = Periodo
    template_name = 'periodo/cadastrar.html'
    form_class = PeriodoForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Periodo cadastrato com sucesso!")
        return reverse('listar-periodo')

class PeriodoUpdateView(UpdateView):
    model = Periodo
    template_name = 'periodo/atualizar.html'
    form_class = PeriodoForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Periodo atualizado com sucesso!")
        return reverse('listar-periodo')

class PeriodoDeleteView(DeleteView):
    model = Periodo
    template_name = 'periodo/periodo_confirm_delete.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Periodo deletado com sucesso!")
        return reverse('listar-periodo')
