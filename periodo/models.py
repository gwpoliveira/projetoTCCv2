from django.db import models

# Create your models here.

class Periodo(models.Model):
    
    periodo = models.CharField('Periodo',unique=True,max_length=10)
    
    def __str__(self):
        return f'{self.id} {self.periodo}'
    
