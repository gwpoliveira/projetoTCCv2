from django.db import models
from periodo.models import Periodo

class Disciplina(models.Model):
    periodo = models.ForeignKey(Periodo, verbose_name='Periodo', on_delete=models.CASCADE)
    disciplina = models.CharField('Disciplina', max_length=200, blank=False)
    
    def __str__(self):
        return f'{self.periodo} {self.disciplina}'