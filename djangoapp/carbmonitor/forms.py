from django import forms
from .models import Refeicao

class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = ['horario']