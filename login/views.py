from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView,View
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm,UserUpdateForm,PassowordUpdateForm
from django.urls import reverse_lazy,reverse
from .models import User
from blog.models import ZisuiPost
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
        
        #自炊履歴と投稿一覧の取り出し
        post_record_list =ZisuiPost.objects.filter(author__username=self.request.user.username).order_by("created") #作られのが早い順に並べたもの
        post_record =ZisuiPost.objects.filter(author__username=self.request.user.username).order_by("-created")#作られたのが遅い順に並べたもの
        post_list = ZisuiPost.objects.filter(author__username=self.request.user.username).exclude(image = "images/1087_01.jpg").order_by("created")

        #総自炊回数の更新
        user.zisui_count = len(post_record)

        if len(post_record)>0:

            #最後に自炊した日の取り出し
            recent_created_at = ZisuiPost.objects.values("created").filter(author__username = user.username).order_by("created").last()
            user.recent_created_at = recent_created_at["created"]
            print("最後に自炊した日",user.recent_created_at)

        if len(post_record)>1:
            #連続自炊日数処理
            today = datetime.date.today()
           
    
            print(today)
            
            td = today- recent_created_at['created'] #現在の時間と最後に自炊した日の差分
            td = td.days
            print("現在と最後に自炊した日の差分",td)
            
            new_post_date = post_record[0].created#最後に自炊記録を記録した日
            if td >=2:
                user.consecutive_zisui_count =0
            
            else:  
                count = 0
                consecutive_zisui_count =0
                for post in post_record:
                    print("取り出した投稿",post,post.created)
                    if count !=0:
                        td_post = new_post_date - post.created
                        td_post = td_post.days
                        print("時差",td_post)
                        if td_post ==1:
                            consecutive_zisui_count  +=1
                            print("連続自炊日数追加")
                        elif td_post >=2:
                            print("連続にならないから終了")
                            break

                        elif count == 0:
                            print("比較なし")
                        
                    new_post_date = post.created
                    print(str(count)+"番目の最後の記録日:",new_post_date)
                    print("")
                    count +=1
                
                print("連続カウント",consecutive_zisui_count)
                if consecutive_zisui_count >0: #連続カウントが1以上なら1足したものが連続日数になる
                    consecutive_zisui_count +=1

                user.consecutive_zisui_count = consecutive_zisui_count
        else:
            print("投稿がありません")

        context = {
                "logined_user":user,
            }


        if len(post_record)>0:
            context["post_record"] = post_record_list
            context["post_list"] = post_list

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
        
        post_record_list =ZisuiPost.objects.filter(author__username=user_detail.username).order_by("created") #作られのが早い順に並べたもの
        post_record =ZisuiPost.objects.filter(author__username=user_detail.username).order_by("-created")#作られたのが遅い順に並べたもの
        post_list = ZisuiPost.objects.filter(author__username=user_detail.username).exclude(image = "images/1087_01.jpg").order_by("created")

        recent_created_at = ZisuiPost.objects.values("created").filter(author__username = user_detail.username).order_by("created").last()
        user_detail.recent_created_at = recent_created_at["created"]

        #総自炊回数の更新
        user_detail.zisui_count = len(post_record)

        #連続自炊日数処理
        if len(post_record)>0:
    
            #最後に自炊した日の取り出し
            recent_created_at = ZisuiPost.objects.values("created").filter(author__username = user_detail.username).order_by("created").last()
            user_detail.recent_created_at = recent_created_at["created"]
            print("最後に自炊した日",user_detail.recent_created_at)

        if len(post_record)>1:
            #連続自炊日数処理
            today = datetime.date.today()
           
    
            print(today)
            
            td = today- recent_created_at['created'] #現在の時間と最後に自炊した日の差分
            td = td.days
            print("現在と最後に自炊した日の差分",td)
            
            new_post_date = post_record[0].created#最後に自炊記録を記録した日
            if td >=2:
                user_detail.consecutive_zisui_count =0
            
            else:  
                count = 0
                consecutive_zisui_count =0
                for post in post_record:
                    print("取り出した投稿",post,post.created)
                    if count !=0:
                        td_post = new_post_date - post.created
                        td_post = td_post.days
                        print("時差",td_post)
                        if td_post ==1:
                            consecutive_zisui_count  +=1
                            print("連続自炊日数追加")
                        elif td_post >=2:
                            print("連続にならないから終了")
                            break

                        elif count == 0:
                            print("比較なし")
                        
                    new_post_date = post.created
                    print(str(count)+"番目の最後の記録日:",new_post_date)
                    print("")
                    count +=1
                
                print("連続カウント",consecutive_zisui_count)
                if consecutive_zisui_count >0: #連続カウントが1以上なら1足したものが連続日数になる
                    consecutive_zisui_count +=1

                user_detail.consecutive_zisui_count = consecutive_zisui_count
        else:
            print("投稿がありません")

        context = {
           "user_detail":user_detail,
    
        }
        if len(post_record)>0:
            context["post_record"] = post_record_list
            context["post_list"] = post_list

        return render(request, "login/profile.html",context)






