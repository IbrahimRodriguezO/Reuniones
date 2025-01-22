from django.shortcuts import render
# IMPORTACIONES NECESARIAS
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .models import User
from .forms import UserRegisterForm
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm

# Create your views here.
class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        usuario = User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["role"],
            form.cleaned_data["password1"],
            nombres=form.cleaned_data["nombres"],
            apellidos=form.cleaned_data["apellidos"]
        )
        return super(UserRegisterView, self).form_valid(form)
    

class LoginUser(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("reporte_app:add-reporte")
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña incorrectos")
        return super().form_invalid(form)
    
    
class LogoutUser(LogoutView):
    next_page = reverse_lazy("users_app:user-login")
