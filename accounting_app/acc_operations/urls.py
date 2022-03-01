from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from acc_operations import views

admin.site.site_header = ""
admin.site.site_title = ""

urlpatterns = [
    path('purchase-invoices/', views.PurchaseInvoiceList.as_view()),
    path('purchase-invoices/<int:pk>/', views.PurchaseInvoiceDetail.as_view()),
    path('sales-invoices/', views.SalesInvoiceList.as_view()),
    path('sales-invoices/<int:pk>/', views.SalesInvoiceDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)