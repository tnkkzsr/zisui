from django.db import models
from login.models import User
from zisui.settings import AUTH_USER_MODEL
import datetime
from zoneinfo import ZoneInfo

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

        title = models.CharField('料理名', max_length=100) 

        image = models.ImageField('画像',upload_to="images/",default="images/1087_01.jpg")

        tag = models.ManyToManyField(Tag,verbose_name="タグ",blank=False,null=False)

        cost = models.CharField("費用", choices=Cost_choices,max_length=20)

        freetext = models.TextField('説明',default="" ,blank = True, null = True)

        author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="投稿者", null=True)

        created = models.DateTimeField("作成日",editable=True,blank=False,null=False, default=datetime.date.today())
        
        
   

        def __str__(self):
    	    return self.title

