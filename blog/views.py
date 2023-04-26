from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView,View
from .models import ZisuiPost
from login.models import User
from .forms import PostForm,EasyPostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#投稿を作成するためのビュー
class PostCreateView(LoginRequiredMixin,CreateView):

    template_name = "blog/postform.html"
    form_class = PostForm
    
    #投稿者が自動的に自分（現在ログインしているユーザー）になるようにする処理
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     
    def get_success_url(self): 
        
        return reverse('post-detail', kwargs={'pk': self.object.pk})


#投稿なしで自炊記録を行うためのビュー
class ZisuiRecordView(LoginRequiredMixin,CreateView):

    template_name = 'blog/postdone.html'
    form_class = EasyPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self): 
        return reverse('mypage')



#投稿一覧ページに対するビュー
class PostListView(ListView):
    def get(self, request,*args, **kwargs):
        post_list = ZisuiPost.objects.exclude(image = "images/1087_01.jpg").order_by("created")
        context = {
                    "post_list":post_list,
                }
        return render(request, "blog/post_list.html",context)


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
        return reverse('mypage')


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


        
    



    

