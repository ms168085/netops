from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import FormView, View
from .models import User
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'index.html'

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        usuario = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password_1'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido']
        )
        messages.success(self.request, "Usuario registrado.")
        return HttpResponseRedirect(reverse('users_app:index'))
    
    def form_invalid(self, form):
        messages.error(self.request, 'Las contraseñas no coinciden.')
        return super().form_invalid(form)

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:index')

    def form_valid(self, form):
        # Autentico el usuario, si es correcto lo guardo en una variable
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        ) 
        # Proceso de login de Django
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class LogoutUser(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Has cerrado tu sesión.')
        return HttpResponseRedirect(reverse('users_app:user_login'))