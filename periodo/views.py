from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Periodo
from .forms import PeriodoForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PeriodoListView(ListView):
    model = Periodo
    template_name = 'periodo/listar.html'
    context_object_name = 'periodos'
    ordering = '-periodo'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get('pesquisa')

        # Se o botão de limpar pesquisa foi clicado, ignore o parâmetro de pesquisa
        if 'limpar_pesquisa' in self.request.GET:
            pesquisa = ''

        if pesquisa:
            queryset = queryset.filter(periodo__icontains=pesquisa)

        return queryset

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
