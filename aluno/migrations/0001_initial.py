# Generated by Django 4.2.7 on 2023-11-15 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0001_initial'),
        ('curso', '0001_initial'),
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matriculaAluno', models.CharField(max_length=10, unique=True, verbose_name='Matricula:')),
                ('nomeAluno', models.CharField(max_length=250, verbose_name='Nome:')),
                ('emailAluno', models.EmailField(max_length=100, verbose_name='Email:')),
                ('tituloTCC', models.CharField(max_length=250, null=True, verbose_name='Titulo do Trabalho:')),
                ('anexosDocumento', models.FileField(upload_to='media/', verbose_name='Anexar Documentos(anexar em um unico arquivo .pdf):')),
                ('dataEntrega', models.DateField(auto_now=True, verbose_name='Data da Entrega:')),
                ('horaEntrega', models.TimeField(auto_now=True, verbose_name='Hora da Entrega:')),
                ('avatarAluno', models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Foto')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disciplina.disciplina', verbose_name='Disciplina')),
                ('nomeProfessor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='professor.professor', verbose_name='Professor')),
            ],
        ),
    ]
