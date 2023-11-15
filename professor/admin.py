from django.contrib import admin
from .models import Professor

# Register your models here.

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["matriculaProfessor", 'nomeProfessor']
    search_fields = ["matriculaProfessor", 'nomeProfessor']
