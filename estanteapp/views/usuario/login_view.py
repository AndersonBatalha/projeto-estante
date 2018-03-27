from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views import View


class LoginView(View):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

        return redirect('estante:index')