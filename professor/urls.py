from django.contrib import admin
from django.urls import path
from .views import ProfessorListView, ProfessorDetailView, ProfessorCreateView, ProfessorUpdateView, ProfessorDeleteView

urlpatterns = [
    path('professor', ProfessorListView.as_view(), name='listar-professor'),
    path('professor/<int:id>', ProfessorDetailView.as_view(), name='detalhar-professor'),
    path('professor/cadastrar/', ProfessorCreateView.as_view(), name='cadastrar-professor'),
    path('professor/atualizar/<int:id>', ProfessorUpdateView.as_view(), name='atualizar-professor'),
    path('professor/deletar/<int:id>', ProfessorDeleteView.as_view(), name='deletar-professor'),
    
]