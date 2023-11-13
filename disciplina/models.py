from django.db import models
from models import Periodo

# Create your models here.
# Tela Disciplina: período, curso e disciplina

class Disciplina():
    periodo = models.ForeignKey('Periodo:', max_length=10, blank=False)
    disciplina = models.CharField('Disciplina', max_length=200, blank=False)
    
    def __str__(self):
        return self.periodo+ ' '+self.disciplina
    