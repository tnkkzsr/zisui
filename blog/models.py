from django.db import models
from login.models import User
from zisui.settings import AUTH_USER_MODEL

Cost_choices = [
    ("費用を選択してください", "費用を選択してください"),
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
    image = models.ImageField('画像',upload_to="images/",default="", blank = True, null = True)
    tag = models.ManyToManyField(Tag,verbose_name="タグ")
    cost = models.CharField("費用", choices=Cost_choices,max_length=20,default="費用を選択してください")
    
    
    ingredients = models.TextField('材料',max_length=128, 
                                    default='''1:                                       
2:
3:
4:
5:
6:
''')
    cost = models.CharField("費用", choices=Cost_choices,max_length=20,default="費用を選択してください")

    howtocook = models.TextField('作り方',default='''手順1:                                       
手順2:
手順3:
手順4:
手順5:
手順6:
''' ,null=False)
    freetext = models.TextField('コメント',default="コメントを入力" ,blank = True, null = True)
    author = models.ForeignKey(User,
                               verbose_name ="投稿者",
                               on_delete=models.CASCADE)

    def __str__(self):
    	return self.title

