from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserLoginForm
from django.views.generic import View


class UserLogin(View):
    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Ошибка авторизации')
        return render(request, 'users/login.html', {"form": form})

    def get(self, request):
        return render(request, 'users/login.html', {"form": UserLoginForm(data=request.POST)})


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
