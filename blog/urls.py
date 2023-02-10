from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    
    path('post/', views.PostCreateView.as_view(), name="post"),
    path('post-list/', views.PostListView.as_view(), name="post-list"),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name="post-update"),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name="post-delete"),
    


    
]