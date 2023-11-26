from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tcc
from .forms import TccForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class TccListView(ListView):
    model = Tcc
    template_name = 'tcc/listar.html'
    context_object_name = 'tccs'
    ordering = '-id'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get('pesquisa')

        # Se o botão de limpar pesquisa foi clicado, ignore o parâmetro de pesquisa
        if 'limpar_pesquisa' in self.request.GET:
            pesquisa = ''

        if pesquisa:
            queryset = queryset.filter(tcc__icontains=pesquisa)

        return queryset

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
    template_name = 'tcc/tcc_confirm_delete.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Tcc deletado com sucesso!")
        return reverse('listar-tcc')