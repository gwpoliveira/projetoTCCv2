# Generated by Django 4.2.7 on 2023-11-26 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('aluno', '0001_initial'),
        ('periodo', '0001_initial'),
        ('tcc', '0002_remove_tcc_titulotcc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tcc',
            name='nomeAluno',
        ),
        migrations.AddField(
            model_name='tcc',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tcc_set', to='aluno.aluno', verbose_name='Aluno'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='membro01',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membro01_tcc_set', to='professor.professor', verbose_name='Presidente da Banca'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='membro02',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='membro02_tcc_set', to='professor.professor', verbose_name='Membro 01'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='membro03',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='membro03_tcc_set', to='professor.professor', verbose_name='Membro 02'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='orientador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orientador_tcc_set', to='professor.professor', verbose_name='Orientador'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periodo.periodo', verbose_name='Período'),
        ),
    ]
