from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View

from estanteapp.forms import LivroForm
from estanteapp.models import ProfessorModel


class CadastroLivroView(View):

    template = 'livro/cadastro_livro.html'

    def get(self, request):
        form = LivroForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            if request.user.get_username() in str(User.objects.get(groups=0)):
                raise PermissionDenied
            dono = ProfessorModel.objects.get(username=request.user)
            livro.dono = dono
            livro.save()
            return redirect('estante:index')

        return render(request, self.template, {'form': form})