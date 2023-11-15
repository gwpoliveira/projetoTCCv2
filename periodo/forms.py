from django.forms import ModelForm
from .models import Periodo


class PeriodoForm(ModelForm):
   
    class Meta:
        model=Periodo
        fields='__all__'