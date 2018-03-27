from django import forms
from django.forms import ModelForm

from estanteapp.models import ProfessorModel


class ProfessorForm(ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'True'}
        )
    )

    def save(self, commit=True):
        user = super(ProfessorForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

    class Meta:
        model = ProfessorModel
        exclude = ('email', "date_joined", 'is_staff',
        'user_permissions', 'groups', 'last_login',
        'last_name', 'is_superuser', 'is_active')