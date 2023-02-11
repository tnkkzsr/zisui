from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import ZisuiPost
from login.models import User
from .forms import PostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timezone

#投稿を作成するためのビュー
class PostCreateView(LoginRequiredMixin,CreateView):

    
    template_name = "blog/postform.html"
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        #自炊カウントを増やす処理
        post_user = self.request.user
        post_user.zisui_count +=1
        
        post_user.save()

        
        return reverse('post-detail', kwargs={'pk': self.object.pk})


#投稿一覧ページに対するビュー
class PostListView(ListView):
    model = ZisuiPost
    context_object_name = "post_list"
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = ZisuiPost
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = ZisuiPost
    form_class = PostForm
    context_object_name = "post_detail"
    template_name = "blog/post-update.html"
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = ZisuiPost
    context_object_name = "post_detail"
    template_name ="blog/delete.html"
    success_url = reverse_lazy("post-list")

#マイページに自分が投稿した自炊記録を表示させるビュー
class MypageListView(ListView):

    model = ZisuiPost
    def get_queryset(self):    
        return super().get_queryset().filter(author__username=self.request.user.username)
    context_object_name = "post_list"
    template_name = "login/mypage.html"




    

