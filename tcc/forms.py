from django.forms import ModelForm
from .models import Tcc


class TccForm(ModelForm):
   
    class Meta:
        model=Tcc
        fields='__all__'