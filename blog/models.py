from django.db import models

# Create your models here.

#
class ZisuiPost(models.Model):



    title = models.CharField('タイトル', max_length=128) 
    image = models.ImageField('画像',upload_to="images/",default="", blank = True, null = True)
    author = models.CharField('投稿者',max_length=128,default="匿名")
    ingredients = models.CharField('材料',max_length=128, default="材料を入力")
    cost = models.IntegerField('費用', default=0)
    howtocook = models.TextField('作り方',default="説明を入力" ,null=False)
    freetext = models.TextField('説明',default="説明を入力" ,null=False)


    def __str__(self):
    	return self.title