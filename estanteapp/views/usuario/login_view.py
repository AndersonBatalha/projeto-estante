from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View


class LoginView(View):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            grupo_usuario = User.objects.get(username=user).groups.all()
            request.session['grupo'] = str(grupo_usuario[0].name)

        return redirect('estante:index')