from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms.professor_form import ProfessorForm
from estanteapp.models import ProfessorModel


class CadastroProfessorView(View):
    template = 'professor/cadastro_professor.html'

    def get(self, request):
        form = ProfessorForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            aluno = ProfessorModel.objects.latest('id')
            aluno.groups.add(1)
            aluno.save()
            return redirect('estante:index')

        return render(request, self.template, {'form': form})