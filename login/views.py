from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView,CreateView
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.urls import reverse_lazy



# Create your views here.


class Login(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm 

class Louout(LogoutView):
    template_name = "login/logout.html"

class Mypage(LoginRequiredMixin,TemplateView):
    template_name ="login/mypage.html"

class Signup(CreateView):
    template_name ="login/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('mypage')

class LoginedIndex(LoginRequiredMixin,TemplateView):
    template_name = "login/logined_index.html"