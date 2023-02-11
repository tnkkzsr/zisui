from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from blog.models import ZisuiPost

class IndexView(ListView):
    template_name = "index.html"
    model = ZisuiPost
    context_object_name = "post_list"
    
    

