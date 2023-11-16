from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Disciplina
from .forms import DisciplinaForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
# class HomeTemplateView(TemplateView):
#     template_name = 'home.html'
    
#     def get_context_data(self, **kwargs):
        
#         context = super().get_context_data(**kwargs)
#         context['disciplina'] = Disciplina.objects.all()[:5]
        
#         return context

class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'curso/listar.html'
    context_object_name = 'disciplina'
    ordering = '-disciplina'

class DisciplinaDetailView(DetailView):
    model = Disciplina
    template_name = 'disciplina/detalhar.html'
    context_object_name = 'disciplina'
    pk_url_kwarg = 'id'
    
class DisciplinaCreateView(CreateView):
    model = Disciplina
    template_name = 'disciplina/cadastrar.html'
    form_class = DisciplinaForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Disciplina cadastrato com sucesso!")
        return reverse('listar-disciplina')

class CursoUpdateView(UpdateView):
    model = Disciplina
    template_name = 'disciplina/atualizar.html'
    form_class = DisciplinaForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Disciplina atualizado com sucesso!")
        return reverse('listar-disciplina')

class DisciplinaDeleteView(DeleteView):
    model = Disciplina
    template_name = 'disciplina/disciplina_confirm_delete.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Disciplina deletado com sucesso!")
        return reverse('listar-disciplina')