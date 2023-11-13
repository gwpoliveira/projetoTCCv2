# Tela Curso: curso

from django.db import models
class Curso():
    cursoId = models.AutoField('Cod. Curso', max_length=10, unique=True, blank=False)
    curso = models.CharField('Curso:', max_length=200, blank=False)
    
# Create your models here.
    def __str__(self):
        return self.idCurso + " " +self.curso
