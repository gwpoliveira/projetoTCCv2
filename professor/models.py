# Tela Professor: matriculaProfessor: nomeProfessor:, 
# emailProfessor:,  curso:, e disciplina:

from django.db import models
from models import Curso
# Create your models here.

matriculaProfessor = models.CharField("Matricula:", max_length=10, unique=True, blank=False)
nomeProfessor = models.CharField("Nome:", max_length=250, blank=False)
emailProfessor = models.EmailField('Email:', max_length=250)
curso = models.ForeignKey("Curso",on_delete=models.CASCADE,blank=True, null=True)