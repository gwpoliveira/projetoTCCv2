# Generated by Django 4.2.7 on 2023-11-26 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='tituloTCC',
        ),
    ]
