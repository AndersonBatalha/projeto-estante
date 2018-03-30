from django.shortcuts import render
from django.views import View

from estanteapp.models import AutorModel


class ListaAutorView(View):
    template = 'autor/lista_autor.html'

    def get(self, request):
        autores = AutorModel.objects.all()
        return render(request, self.template, {'autores': autores})