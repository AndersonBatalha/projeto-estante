from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms import AutorForm
from django.contrib.auth.models import User

class CadastroAutorView(View):
    template = 'autor/cadastro_autor.html'

    def get(self, request):
        if not request.user.is_authenticated or request.session['grupo'] not in str(User.objects.get(groups=1)):
            raise PermissionDenied
        form = AutorForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('estante:index')
        return render(request, self.template, {'form': form})