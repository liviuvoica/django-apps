from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from newsletter_api import views

admin.site.site_header = ""
admin.site.site_title = ""

urlpatterns = [
    path('newsletter/', views.NewsletterList.as_view()),
    path('newsletter/<int:pk>/', views.NewsletterListDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)