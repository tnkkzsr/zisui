from django.contrib import admin
from django.urls import path,include
from .views import Login,Louout,MypageView,Signup,UserUpdateView,PasswordUpdateView,UserListView,UserDetailView




urlpatterns = [
    
    path('login/',Login.as_view(), name="login"),
    path('logout/',Louout.as_view(), name= "logout"),
    path('mypage/',MypageView.as_view(), name= "mypage"),
    path('signup/',Signup.as_view(), name= "signup"),
    path('user-update/<int:pk>/',UserUpdateView.as_view(), name= "user-update"),
    path('password-update/<int:pk>/',PasswordUpdateView.as_view(), name= "password-update"),
    path('user-list/', UserListView.as_view(), name="user-list"),
    path('user-detail/<int:pk>/',UserDetailView.as_view(), name= "user-detail"),
  
]
