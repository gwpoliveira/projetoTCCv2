from django.db import models
from models import Curso,Disciplina,Professor


# Tela Aluno: poderá cadastrar: matriculaAluno, nomeAluno:, emailAluno:, 
# curso:, disciplina:, professor:, tituloTCC:, anexosDocumento:, dataEntrega e 
# horaEntrega: , se a data estiver liberada poderá inserir o anexosDocumento, c
# aso contrário o anexosDocumento:, dataEntrega e horaEntrega  ficara desabilitado.
# Create your models here.

class Aluno(models.Model):
    matriculaAluno = models.CharField("Matricula:", max_length=10, unique=True, blank=False)
    nomeAluno = models.CharField("Nome:", max_length=250, blank=False)
    emailAluno = models.EmailField('Email:', max_length=100, blank=False)
    curso = models.ForeignKey("Curso",on_delete=models.CASCADE,blank=True, null=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE,blank=True, null=True)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE,blank=True, null=True)
    tituloTCC = models.CharField('Titulo do Trabalho:', max_length=250, blank=False, null=True)
    anexosDocumento = models.FileField("Anexar Documentos(anexar em um unico arquivo .pdf):",upload_to='media/', blank=False) 
    dataEntrega = models.DateField('Data da Entrega:', auto_now=True)
    horaEntrega = models.TimeField('Hora da Entrega:',auto_now=True)
    

    def __str__(self):
        return self.matriculaAluno + " " +self.nomeAluno
