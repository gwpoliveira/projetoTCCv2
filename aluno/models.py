from django.db import models
from curso.models import Curso
from disciplina.models import Disciplina
from professor.models import Professor


class Aluno(models.Model):
    matriculaAluno = models.CharField("Matricula:", max_length=10, unique=True, blank=False)
    nomeAluno = models.CharField("Nome:", max_length=250, blank=False)
    emailAluno = models.EmailField('Email:', max_length=100, blank=False)
    curso = models.ForeignKey(Curso,verbose_name="Curso",on_delete=models.CASCADE,blank=True, null=True)
    disciplina = models.ForeignKey(Disciplina,verbose_name='Disciplina', on_delete=models.CASCADE,blank=True, null=True)
    nomeProfessor = models.ForeignKey(Professor,verbose_name='Professor', on_delete=models.CASCADE,blank=True, null=True)
    tituloTCC = models.CharField('Titulo do Trabalho:', max_length=250, blank=False, null=True)
    anexosDocumento = models.FileField("Anexar Documentos(anexar em um unico arquivo .pdf):",upload_to='media/', blank=False) 
    dataEntrega = models.DateField('Data da Entrega:', auto_now=True,blank=False)
    horaEntrega = models.TimeField('Hora da Entrega:',auto_now=True,blank=False)
    avatarAluno = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)
    

    def __str__(self):
        return f'{self.matriculaAluno} {self.nomeAluno}'
