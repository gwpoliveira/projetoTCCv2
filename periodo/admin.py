from django.contrib import admin
from .models import Periodo

# Register your models here.

@admin.register(Periodo)
class Periodo(admin.ModelAdmin):
    list_display = ["periodo"]
    search_fields = ['periodo']