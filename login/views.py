from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm,UserUpdateForm,PassowordUpdateForm
from django.urls import reverse_lazy,reverse
from .models import User
from blog.models import ZisuiPost



# Create your views here.


class Login(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm 

class Louout(LogoutView):
    template_name = "login/logout.html"

class Mypage(LoginRequiredMixin,TemplateView):
    template_name ="login/mypage.html"
    context_object_name = "user_detail"
    def user_info(request):
        user = request.user
        
        render(request,"login/mypage.html", {"user":user})
    
class Signup(CreateView):
    template_name ="login/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('mypage')

#ユーザー情報を更新するためのビュー
class UserUpdateView (UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "login/user_update.html"

    def user_info(request):
        user = request.user
        render(request,"login/user_upadate.html", {"user":user})

    def get_success_url(self):
        return reverse('mypage')

#パスワード、メールアドレスを更新するためのビュー
class PasswordUpdateView (UpdateView):
    model = User
    form_class = PassowordUpdateForm
    template_name = "login/password_update.html"

    def user_info(request):
        user = request.user
        render(request,"login/user_upadate.html", {"user":user})

    def get_success_url(self):
        return reverse('mypage')
   
#ユーザー一覧を表示するビュー
class UserListView(ListView):
    model = User
    template_name = "login/user_list.html"
    context_object_name = "user_list"

#ユーザー詳細を表示するビュー
class UserDetailView(DetailView):
    model = User
    template_name = "login/profile.html"
    context_object_name = "user_detail"



    

