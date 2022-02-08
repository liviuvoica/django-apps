from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contact_api import views

admin.site.site_header = ""
admin.site.site_title = ""

urlpatterns = [
    path('contact-me/', views.ContactList.as_view()),
    path('contact-me/<int:pk>/', views.ContactDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)