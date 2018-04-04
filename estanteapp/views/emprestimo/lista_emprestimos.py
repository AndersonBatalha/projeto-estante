from django.shortcuts import render
from django.views import View

from estanteapp.models import EmprestimoModel


class ListaEmprestimosView(View):
    template = 'emprestimo/lista_emprestimos.html'
    def get(self, request):
        emprestimos = EmprestimoModel.objects.all()
        return render(request, self.template, {'emprestimos': emprestimos})