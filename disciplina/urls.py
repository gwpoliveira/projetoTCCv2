from django.contrib import admin
from django.urls import path
from .views import DisciplinaListView, DisciplinaDetailView, DisciplinaCreateView, DisciplinaUpdateView, DisciplinaDeleteView

urlpatterns = [
    path('disciplina', DisciplinaListView.as_view(), name='listar-disciplina'),
    path('disciplina/<int:id>', DisciplinaDetailView.as_view(), name='detalhar-disciplina'),
    path('disciplina/cadastrar/', DisciplinaCreateView.as_view(), name='cadastrar-disciplina'),
    path('disciplina/atualizar/<int:id>', DisciplinaUpdateView.as_view(), name='atualizar-disciplina'),
    path('disciplina/deletar/<int:id>', DisciplinaDeleteView.as_view(), name='deletar-disciplina'),
    
]