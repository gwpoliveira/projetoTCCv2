from django.forms import ModelForm
from .models import Tcc


class TccForm(ModelForm):
   
    class Meta:
        model=Tcc
        fields='__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        pesquisa = cleaned_data.get('pesquisa')

        # Se o botão de limpar pesquisa for clicado, limpar o campo de pesquisa
        if 'limpar_pesquisa' in self.data:
            cleaned_data['pesquisa'] = ''

        return cleaned_data