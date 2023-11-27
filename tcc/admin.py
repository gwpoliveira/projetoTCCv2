from django.contrib import admin
from .models import Tcc

# Register your models here.

@admin.register(Tcc)
class TccAdmin(admin.ModelAdmin):
    list_display = ["periodo", 'disciplina', 'nomeAluno','orientador', 'membro01', 'membro02', 'membro03']
    search_fields = ["nomeAluno", 'orientador']
