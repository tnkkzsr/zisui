from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,UserManager


Gradechoices = [
    
    ("大学1年", "大学1年"),
    ("大学2年", "大学2年"),
    ("大学3年", "大学3年"),
    ("大学4年", "大学4年"),
    ("大学院1年", "大学院1年"),
    ("大学院2年", "大学院2年"),
    ("社会人", "社会人"),
    ("その他", "その他"),

]

Livingalonechoice = [
    
    ("1年", "1年"),
    ("2年", "2年"),
    ("3年", "3年"),
    ("4年", "4年"),
    ("5年", "5年"),
    ("6年", "6年"),
    ("7年以上", "7年以上"),

]

#独自のユーザーモデルを定義
class User(AbstractBaseUser):
    
    email = models.EmailField('Eメールアドレス(ログイン時に使用）', max_length=255, unique=True,)
    username = models.CharField('ニックネーム', max_length=128,default="")
    userimage = models.ImageField('プロフィール画像',upload_to="images/", default="")
    years =  models.CharField('学年', max_length=128,choices=Gradechoices,default="大学1年")
    living_alone = models.CharField('一人暮らし歴', max_length=128,choices =Livingalonechoice,default="1年")
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
    active = models.BooleanField(default=True)
    zisui_count = models.IntegerField("総自炊回数",default=0)
    consecutive_zisui_count = models.IntegerField("総自炊回数",default=0)
    

    
    USERNAME_FIELD = 'email'

    objects = UserManager()
    
    
    def __str__(self):             
        return self.username

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_staff(self):
        return self.staff


    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


