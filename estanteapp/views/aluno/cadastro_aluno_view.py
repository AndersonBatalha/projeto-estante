from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms.aluno_form import AlunoForm
from estanteapp.models import AlunoModel


class CadastroAlunoView(View):
    template = 'aluno/cadastro_aluno.html'

    def get(self, request):
        form = AlunoForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            aluno = AlunoModel.objects.latest('id')
            aluno.groups.add(0)
            aluno.save()
            return redirect('estante:index')

        return render(request, self.template, {'form': form})

