# Generated by Django 4.2.7 on 2023-11-26 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
        ('tcc', '0004_alter_tcc_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcc',
            name='tituloTCC',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tituloTCC_tcc_set', to='aluno.aluno', verbose_name='Titulo do TCC:'),
        ),
    ]
