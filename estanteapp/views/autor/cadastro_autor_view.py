from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms import AutorForm


class CadastroAutorView(View):
    template = 'autor/cadastro_autor.html'

    def get(self, request):
        form = AutorForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estante:index')
        return render(request, self.template, {'form': form})