from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Curso
from .forms import CursoForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class CursoListView(ListView):
    model = Curso
    template_name = 'curso/listar.html'
    context_object_name = 'cursos'
    ordering = '-curso'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'curso/detalhar.html'
    context_object_name = 'curso'
    pk_url_kwarg = 'id'
    
class CursoCreateView(CreateView):
    model = Curso
    template_name = 'curso/cadastrar.html'
    form_class = CursoForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Curso cadastrato com sucesso!")
        return reverse('listar-curso')

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'curso/atualizar.html'
    form_class = CursoForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Curso atualizado com sucesso!")
        return reverse('listar-curso')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'curso/curso_confirm_delete.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Curso deletado com sucesso!")
        return reverse('listar-curso')