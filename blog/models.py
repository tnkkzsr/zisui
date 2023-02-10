from django.db import models
from login.models import User
from zisui.settings import AUTH_USER_MODEL

Cost_choices = [

    
    ("0~100円", "0~100円"),
    ("100~200円", "100~200円"),
    ("200~300円", "200~300円"),
    ("300~400円", "300~400円"),
    ("500~600円", "500~600円"),
    ("600~700円", "600~700円"),
    ("700~800円", "700~800円"),
    ("800~900円", "800~900円"),
    ("900~1000円", "900~1000円"),
    ("1000円以上", "1000円以上"),
    ("不明", "不明"),
]

class Tag(models.Model):
        name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        default="")
    
        def __str__(self):
            return self.name


class ZisuiPost(models.Model):

        title = models.CharField('タイトル', max_length=100) 

        image = models.ImageField('画像',upload_to="images/",default="")

        tag = models.ManyToManyField(Tag,verbose_name="タグ",blank=False,null=False)

        cost = models.CharField("費用", choices=Cost_choices,max_length=20)


        freetext = models.TextField('説明',default="" ,blank = True, null = True)

        author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="投稿者", null=True)

        created = models.DateTimeField("作成日",auto_now_add=True,editable=False,blank=False,null=False)
        updated = models.DateTimeField(auto_now=True,editable=False,blank=True,null=True)

   

        def __str__(self):
    	    return self.title

