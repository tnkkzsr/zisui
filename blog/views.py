from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView,View
from .models import ZisuiPost
from login.models import User
from .forms import PostForm,EasyPostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timezone
import datetime
#from django.utils.timezone import make_aware
from zoneinfo import ZoneInfo


#投稿を作成するためのビュー
class PostCreateView(LoginRequiredMixin,CreateView):

    template_name = "blog/postform.html"
    form_class = PostForm
    
    #投稿者が自動的に自分（現在ログインしているユーザー）になるようにする処理
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     
    def get_success_url(self): 
        post_user = self.request.user #自炊カウントを増やす処理
        post_user.zisui_count +=1  
        post_user.save()
        return reverse('post-detail', kwargs={'pk': self.object.pk})


#投稿なしで自炊記録を行うためのビュー
class ZisuiRecordView(LoginRequiredMixin,CreateView):

    template_name = 'blog/postdone.html'
    form_class = EasyPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self): 
        post_user = self.request.user #自炊カウントを増やす処理
        post_user.zisui_count +=1  

        #連続処理
        # now_date = self.object.created#datetime.datetime.now(ZoneInfo("Asia/Tokyo")) #現在の日時
        # second_recent_created_at = post_user.recent_created_at #投稿処理を行う前の最新の投稿日時
        # second_recent_created_at_day = second_recent_created_at.day #投稿処理を行う前の最新の投稿日の日付
        # td= now_date.day - second_recent_created_at_day #投稿を行った現在の日付と、投稿処理を行う前の最新の投稿日の日付の差
        # print(second_recent_created_at)
        # print(now_date)
        # print(td)
        # if  td==1:
        #      post_user.consecutive_zisui_count += 1 


        #最後の投稿日を更新
        # recent_created_at = ZisuiPost.objects.values("created").filter(author__username = post_user.username).order_by("created").last()
        # post_user.recent_created_at = recent_created_at["created"]
        # print(post_user.recent_created_at.day)


        post_user.save()

        return reverse('mypage')

    




#投稿一覧ページに対するビュー
class PostListView(ListView):
    model = ZisuiPost
    context_object_name = "post_list"
    template_name = "blog/post_list.html"

#投稿詳細（編集不可）のページに飛ぶビュー
class PostDetailView(DetailView):
    model = ZisuiPost
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"


#投稿を編集するためのビュー
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = ZisuiPost
    form_class = PostForm
    context_object_name = "post_detail"
    template_name = "blog/post-update.html"
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

#投稿を削除するためのビュー
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = ZisuiPost
    context_object_name = "post_detail"
    template_name ="blog/delete.html"

    def get_success_url(self): 
        post_user = self.request.user
        post_user.zisui_count -=1
        recent_created_at = ZisuiPost.objects.values("created").filter(author__username = post_user.username).order_by("created").last()
        post_user.recent_created_at = recent_created_at["created"]
        post_user.save()

        
        return reverse('mypage')

    # success_url = reverse_lazy("mypage")

#投稿詳細（編集可能）に飛ぶビュー
class MyPostDetailView(DetailView):
    model = ZisuiPost
    context_object_name = "post_detail"
    template_name = "blog/mypost_detail.html"

#ユーザー詳細に、そのユーザーが投稿した自炊記録を一覧表示させるビュー
class UserPostView(ListView):
    model = ZisuiPost
    context_object_name = "post_list"
    template_name = "login/profile.html"


        
    



    

