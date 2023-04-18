from django.shortcuts import render
from django.views.generic import View
from blog.models import ZisuiPost

class IndexView(View):
    
    def get(self, request,*args, **kwargs):

        post_record =ZisuiPost.objects.exclude(image = "images/1087_01.jpg").order_by("-id")#作られたのが遅い順に並べたもの
        context = {
                "post_list":post_record,
            }

        return render(request, "index.html",context)
   
    

    
    
    

