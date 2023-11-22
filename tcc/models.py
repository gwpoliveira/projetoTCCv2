from django.db import models
from periodo.models import Periodo
from disciplina.models import Disciplina
from aluno.models import Aluno
from professor.models import Professor

# Create your models here.
class Tcc(models.Model):
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo", on_delete=models.CASCADE, blank=False)
    disciplina = models.ForeignKey(Disciplina, verbose_name="Disciplina", on_delete=models.CASCADE, blank=False)
    nomeAluno = models.ForeignKey(Aluno, related_name='nomeAluno_tcc_set',verbose_name="Aluno:",on_delete=models.CASCADE, blank=False, null=True)
    tituloTCC = models.ForeignKey(Aluno, related_name='tituloTCC_tcc_set',verbose_name="Titulo do TCC:",on_delete=models.CASCADE, blank=False, null=True)
    orientador = models.ForeignKey(Professor, related_name='orientador_tcc_set',verbose_name='Orientador:', on_delete=models.CASCADE, blank=False)
    membro01 = models.ForeignKey(Professor, related_name='membro01_tcc_set',verbose_name='Presidente da Banca:', on_delete=models.CASCADE, blank=False)
    membro02 = models.ForeignKey(Professor, related_name='membro02_tcc_set',verbose_name='Membro 01:', on_delete=models.CASCADE, blank=True)
    membro03 = models.ForeignKey(Professor, related_name='membro03_tcc_set',verbose_name='Menbro 02:', on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f'{self.periodo} {self.disciplina} {self.nomeAluno} {self.tituloTCC} {self.orientador} {self.membro01} {self.membro02} {self.membro03}'