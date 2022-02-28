from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from acc_suppliers_and_clients import views

admin.site.site_header = ""
admin.site.site_title = ""

urlpatterns = [
    path('suppliers/', views.SupplierList.as_view()),
    path('suppliers/<int:pk>/', views.SupplierDetail.as_view()),
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)