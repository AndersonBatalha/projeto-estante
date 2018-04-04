from django.shortcuts import render, redirect
from django.views import View

from estanteapp.models import AlunoModel


class EmprestimoLivroView(View):
    template = "emprestimo/emprestimo_livro.html"

    def get(self, request):
        form = EmprestimoForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save()
            aluno = AlunoModel.objects.get(username=request.user)
            emprestimo.aluno = aluno
            emprestimo.save()
            return redirect('estante:index')

        return render(request, self.template, {'form': form})
