from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['aluno'] = Aluno.objects.all()[:5]
        return context

class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno/listar.html'
    context_object_name = 'alunos'
    ordering = '-nomeAluno'

class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'aluno/detalhar.html'
    context_object_name = 'aluno'
    pk_url_kwarg = 'id'
    
class AlunoCreateView(CreateView):
    model = Aluno
    template_name = 'aluno/cadastrar.html'
    form_class = AlunoForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Aluno cadastrato com sucesso!")
        return reverse('listar-aluno')

class AlunoUpdateView(UpdateView):
    model = Aluno
    template_name = 'aluno/atualizar.html'
    form_class = AlunoForm
    id_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Aluno atualizado com sucesso!")
        return reverse('listar-aluno')

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_confirm_delete.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Aluno deletado com sucesso!")
        return reverse('listar-aluno')