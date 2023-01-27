from django.contrib import admin
from django.urls import path,include
from .views import Login,Louout,Mypage,Signup,LoginedIndex



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',Login.as_view(), name="login"),
    path('logout/',Louout.as_view(), name= "logout"),
    path('mypage/',Mypage.as_view(), name= "mypage"),
    path('signup/',Signup.as_view(), name= "signup"),
    path('logined-index', LoginedIndex.as_view(), name="loginindex")


    
   
  
]
