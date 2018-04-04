
from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms import AutorForm
from estanteapp.models import AutorModel


class EdicaoAutorView(View):
    template = 'autor/cadastro_autor.html'
    def get(self, request, id=None):
        autor = AutorModel.objects.get(pk=id)
        form = AutorForm(instance=autor)
        context_dict = {'form': form, 'id': id}
        return render(request, self.template, context_dict)

    def post(self, request, id=None):
        autor = AutorModel.objects.get(pk=id)
        form = AutorForm(instance=autor, data=request.POST)
        context_dict = {'form': form, 'id': id}
        if form.is_valid():
            form.save()
            return redirect("estante:lista_autor")
        return render(request, self.template, context_dict)

