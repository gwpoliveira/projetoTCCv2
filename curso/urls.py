from django.contrib import admin
from django.urls import path
from .views import CursoListView, CursoDetailView, CursoCreateView, CursoUpdateView, CursoDeleteView

urlpatterns = [
    path('curso', CursoListView.as_view(), name='listar-curso'),
    path('curso/<int:id>', CursoDetailView.as_view(), name='detalhar-curso'),
    path('curso/cadastrar/', CursoCreateView.as_view(), name='cadastrar-curso'),
    path('curso/atualizar/<int:id>', CursoUpdateView.as_view(), name='atualizar-curso'),
    path('curso/deletar/<int:id>', CursoDeleteView.as_view(), name='deletar-curso'),
    
]