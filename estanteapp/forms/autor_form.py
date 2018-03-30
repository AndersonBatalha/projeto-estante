from django.forms import ModelForm

from estanteapp.models import AutorModel


class AutorForm(ModelForm):

    class Meta:
        model = AutorModel
        fields = '__all__'
