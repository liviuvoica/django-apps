from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog_api import views

admin.site.site_header = "Blog API Dashboard"
admin.site.site_title = "Blog API"

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)