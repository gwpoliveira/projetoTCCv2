from django.db import models
from periodo.models import Periodo
from curso.models import Curso

class Disciplina(models.Model):
    periodo = models.ForeignKey(Periodo, verbose_name='Periodo', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,verbose_name='Curso', on_delete=models.CASCADE, blank=True, null=True)
    disciplina = models.CharField('Disciplina', max_length=200, blank=False)
    
    def __str__(self):
        return f'{self.periodo} {self.curso} {self.disciplina}'