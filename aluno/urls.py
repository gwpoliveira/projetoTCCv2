from django.contrib import admin
from django.urls import path
from .views import AlunoListView, AlunoDetailView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView

urlpatterns = [
    path('aluno', AlunoListView.as_view(), name='listar-aluno'),
    path('aluno/<int:id>', AlunoDetailView.as_view(), name='detalhar-aluno'),
    path('aluno/cadastrar/', AlunoCreateView.as_view(), name='cadastrar-aluno'),
    path('aluno/atualizar/<int:id>', AlunoUpdateView.as_view(), name='atualizar-aluno'),
    path('aluno/deletar/<int:id>', AlunoDeleteView.as_view(), name='deletar-aluno'),
    
]