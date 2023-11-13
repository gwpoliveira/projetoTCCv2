from django.db import models

# Create your models here.

class Periodo():
    periodo = models.CharField('Periodo',unique=True,blank=False,max_length=10)
    
    def __str__(self):
        return self.periodo
    
