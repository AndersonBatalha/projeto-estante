from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms.professor_form import ProfessorForm


class CadastroProfessorView(View):
    template = 'professor/cadastro_professor.html'

    def get(self, request):
        form = ProfessorForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estante:index')
        return render(request, self.template, {'form': form})