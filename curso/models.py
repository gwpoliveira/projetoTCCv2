# Tela Curso: curso

from django.db import models
class Curso(models.Model):
    
    curso = models.CharField('Curso:', max_length=100, blank=False)
    
# Create your models here.
    def __str__(self):
        return f'{self.id} {self.curso}'
