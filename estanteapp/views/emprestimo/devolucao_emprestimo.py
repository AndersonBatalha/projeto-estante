from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View

from estanteapp.models import EmprestimoModel


class DevolucaoEmprestimoView(View):
    template = 'emprestimo/devolucao_emprestimo.html'

    def get(self, request):
        emprestimos = EmprestimoModel.objects.filter(aluno=request.user.id, devolvido=False)
        return render(request, self.template, {'emprestimos': emprestimos})

    def post(self, request):
        emprestimo = EmprestimoModel.objects.get(pk=request.POST['id_emprestimo'])
        emprestimo.dia_devolucao = datetime.datetime.now().date()
        emprestimo.devolvido = True
        emprestimo.save()
        return redirect('estante:devolucao_emprestimo')