from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

from accounts.forms import (
    RegisterForm,
    LoginForm
)



class RegisterView(View):
    def get(self, request):
        form = RegisterForm()

        context = {
            'form': form,
        }

        return render(request, 'accounts/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Qeydiyyatdan keçildi')
            return redirect('home')
        
        else:
            messages.error(request, form.errors)
            return redirect('register')



class LoginView(View):
    def get(self, request):
        form = LoginForm()

        context = {
            'form': form,
        }

        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)

                messages.success(request, 'Daxil olundu')
                return redirect('home')
            
            else:
                messages.info(request, 'İstifadəçi adı və ya şifrə yanlışdır')
                return redirect('login')
        else:
            messages.error(request, form.errors)
            return redirect('login')



class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)

        messages.success(request, 'Hesabdan çıxıldı')
        return redirect('home')