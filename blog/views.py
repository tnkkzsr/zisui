from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .models import ZisuiPost
from .forms import PostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#投稿を作成するためのビュー
class PostCreateView(LoginRequiredMixin,CreateView):

    template_name = "blog/postform.html"
    form_class = PostForm
    success_url = reverse_lazy("postdone")

#投稿すると投稿完了ページに飛ぶビュー
class PostdoneView(TemplateView):
    template_name = "blog/postdone.html"

    

