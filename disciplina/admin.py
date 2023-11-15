from django.contrib import admin
from .models import Disciplina

# Register your models here.

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["periodo",'disciplina']
    search_fields = ['periodo', 'disciplina']