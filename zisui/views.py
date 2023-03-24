from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from blog.models import ZisuiPost

class IndexView(ListView):
    template_name = "index.html"
    model = ZisuiPost
    def get_queryset(self) :
        return super().get_queryset().exclude(image = "images/1087_01.jpg")
    context_object_name = "post_list"


    
    
    

