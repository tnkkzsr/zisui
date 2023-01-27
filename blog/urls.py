from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    
    path('post/', views.PostCreateView.as_view(), name="post"),
    path('postdone/', views.PostdoneView.as_view(), name="postdone"),
    
]