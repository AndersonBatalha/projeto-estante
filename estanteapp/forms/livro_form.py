from django.forms import ModelForm

from estanteapp.models import LivroModel


class LivroForm(ModelForm):
    class Meta:
        model = LivroModel
        fields = ['titulo', 'resumo', 'autor']