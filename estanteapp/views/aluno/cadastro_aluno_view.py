from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms.aluno_form import AlunoForm


class CadastroAlunoView(View):
    template = 'aluno/cadastro_aluno.html'

    def get(self, request):
        form = AlunoForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estante:index')
        return render(request, self.template, {'form': form})
