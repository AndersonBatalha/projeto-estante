from django import forms
from django.forms import ModelForm

from estanteapp.models import AlunoModel


class AlunoForm(ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'True'}
        )
    )

    def save(self, commit=True):
        user = super(AlunoForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

    class Meta:
        model = AlunoModel
        exclude = ('email', "date_joined", 'is_staff',
        'user_permissions', 'groups', 'last_login',
        'last_name', 'is_superuser', 'is_active')