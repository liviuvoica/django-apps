from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from error_and_notification_api import views

admin.site.site_header = ""
admin.site.site_title = ""

urlpatterns = [
    path('error-and-notification/', views.ErrorAndNotificationList.as_view()),
    path('error-and-notification/<int:pk>/', views.ErrorAndNotificationListDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)