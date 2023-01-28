from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView,CreateView,DetailView,ListView
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.urls import reverse_lazy
from .models import User



# Create your views here.


class Login(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm 

class Louout(LogoutView):
    template_name = "login/logout.html"

class Mypage(LoginRequiredMixin,TemplateView):
    template_name ="login/mypage.html"
    context_object_name = "user_detail"
    
    

class Signup(CreateView):
    template_name ="login/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('mypage')



class UserListView(ListView):
    model = User
    context_object_name = "user_list"
    template_name = "login/user_list.html"

   