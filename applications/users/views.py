from django.shortcuts import render
# IMPORTACIONES NECESARIAS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views.generic.edit import FormView
from .models import User
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm, LoginForm

# Create your views here.
class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        usuario = User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password1"],
            nombres=form.cleaned_data["nombres"],
            apellidos=form.cleaned_data["apellidos"]
        )
        return super(UserRegisterView, self).form_valid(form)
    

class LoginUser(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home_app:panel")

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:user-login')
        )
