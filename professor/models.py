# Tela Professor: matriculaProfessor: nomeProfessor:, 
# emailProfessor:,  curso:, e disciplina:

from django.db import models
from curso.models import Curso
# Create your models here.

class Professor(models.Model):
    matriculaProfessor = models.CharField("Matricula:", max_length=10, unique=True, blank=False)
    nomeProfessor = models.CharField("Nome:", max_length=250, blank=False)
    emailProfessor = models.EmailField('Email:', max_length=250)
    curso = models.ForeignKey(Curso,verbose_name="Curso",on_delete=models.CASCADE,blank=True, null=True)
    avatarProfessor = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return f'{self.matriculaProfessor} {self.nomeProfessor}'