from django.contrib import admin
from django.urls import path
from .views import PeriodoListView, PeriodoDetailView, PeriodoCreateView, PeriodoUpdateView, PeriodoDeleteView

urlpatterns = [
    path('periodo', PeriodoListView.as_view(), name='listar-periodo'),
    path('periodo/<int:id>', PeriodoDetailView.as_view(), name='detalhar-periodo'),
    path('periodo/cadastrar/', PeriodoCreateView.as_view(), name='cadastrar-periodo'),
    path('periodo/atualizar/<int:id>', PeriodoUpdateView.as_view(), name='atualizar-periodo'),
    path('periodo/deletar/<int:id>', PeriodoDeleteView.as_view(), name='deletar-periodo'),
    
]