from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from .models import ZisuiPost
from .forms import PostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#投稿を作成するためのビュー
class PostCreateView(LoginRequiredMixin,CreateView):
    
    template_name = "blog/postform.html"
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
            return reverse('post-detail', kwargs={'pk': self.object.pk})

#投稿すると投稿完了ページに飛ぶビュー
class PostdoneView(TemplateView):
    template_name = "blog/postdone.html"

#投稿一覧ページに対するビュー
class PostListView(ListView):
    model = ZisuiPost
    context_object_name = "post_list"
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = ZisuiPost
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"



    

