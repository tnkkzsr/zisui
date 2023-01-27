from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,UserManager

#独自のユーザーモデルを定義
class User(AbstractBaseUser):
    
    email = models.EmailField('Eメールアドレス', max_length=255, unique=True,)
    username = models.CharField('ニックネーム', max_length=128,default="")
    userimage = models.ImageField('画像',upload_to="images/", default="",blank = True, null = True)
    years =  models.CharField('学年', max_length=128,default="大学○年")
    living_alone = models.CharField('一人暮らし歴', max_length=128,default="年")
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
    active = models.BooleanField(default=True)

    
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


