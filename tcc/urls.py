from django.contrib import admin
from django.urls import path
from .views import TccListView, TccDetailView, TccCreateView, TccUpdateView, TccDeleteView

urlpatterns = [
    path('tcc', TccListView.as_view(), name='listar-tcc'),
    path('tcc/<int:id>', TccDetailView.as_view(), name='detalhar-tcc'),
    path('tcc/cadastrar/', TccCreateView.as_view(), name='cadastrar-tcc'),
    path('tcc/atualizar/<int:id>', TccUpdateView.as_view(), name='atualizar-tcc'),
    path('tcc/deletar/<int:id>', TccDeleteView.as_view(), name='deletar-tcc'),
    
]