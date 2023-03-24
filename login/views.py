from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView,View
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm,UserUpdateForm,PassowordUpdateForm
from django.urls import reverse_lazy,reverse
from .models import User
from blog.models import ZisuiPost
from django.utils.timezone import make_aware
import datetime



# Create your views here.


class Login(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm 

class Louout(LogoutView):
    template_name = "login/logout.html"


   
#マイページへのビュー
class MypageView(LoginRequiredMixin,View):

    def get(self, request,*args, **kwargs):
        #現在ログインしているユーザー情報を取得
        user = self.request.user
        recent_created_at = ZisuiPost.objects.values("created").filter(author__username = user.username).order_by("created").last()
        user.recent_created_at = recent_created_at["created"]
        print(user.recent_created_at)
        #自炊履歴と投稿一覧の取り出し
        post_record = ZisuiPost.objects.filter(author__username=self.request.user.username).order_by("created")
        post_list = ZisuiPost.objects.filter(author__username=self.request.user.username).exclude(image = "images/1087_01.jpg").order_by("created")
        #連続日数の削除
        context = {
           "post_record":post_record,
           "post_list":post_list,
            "logined_user":user,

        }

        return render(request, "login/mypage.html",context)
   
    
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

class UserDetailView(View):

    def get(self, request,*args, **kwargs):
        user_detail = User.objects.get(pk=self.kwargs['pk'])
        
        recent_created_at = ZisuiPost.objects.values("created").filter(author__username = user_detail.username).order_by("created").last()
        user_detail.recent_created_at = recent_created_at["created"]
        post_list = ZisuiPost.objects.filter(author__username = user_detail.username).exclude(image = "images/1087_01.jpg")
        post_record = ZisuiPost.objects.filter(author__username=user_detail.username)

        
        context = {
           "user_detail":user_detail,
           "post_list":post_list,
           "post_record":post_record,
        }

        return render(request, "login/profile.html",context)






