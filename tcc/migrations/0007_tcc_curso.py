# Generated by Django 4.2.7 on 2023-11-26 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_alter_curso_curso'),
        ('tcc', '0006_remove_tcc_aluno_tcc_nomealuno_alter_tcc_membro01_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcc',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.curso', verbose_name='Curso'),
        ),
    ]
