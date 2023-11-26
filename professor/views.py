from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Professor
from .forms import ProfessorForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor/listar.html'
    context_object_name = 'professors'
    ordering = '-nomeProfessor'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get('pesquisa')

        # Se o botão de limpar pesquisa foi clicado, ignore o parâmetro de pesquisa
        if 'limpar_pesquisa' in self.request.GET:
            pesquisa = ''

        if pesquisa:
            queryset = queryset.filter(nomeProfessor__icontains=pesquisa)

        return queryset

class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'professor/detalhar.html'
    context_object_name = 'professor'
    pk_url_kwarg = 'id'
    
class ProfessorCreateView(CreateView):
    model = Professor
    template_name = 'professor/cadastrar.html'
    form_class = ProfessorForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Professor cadastrato com sucesso!")
        return reverse('listar-professor')

class ProfessorUpdateView(UpdateView):
    model = Professor
    template_name = 'professor/atualizar.html'
    form_class = ProfessorForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Professor atualizado com sucesso!")
        return reverse('listar-professor')

class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professor/professor_confirm_delete.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Professor deletado com sucesso!")
        return reverse('listar-professor')