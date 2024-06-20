# seminar_dz/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.client_list, name='client_list'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/<int:client_id>/orders/', views.client_orders, name='client_orders'),
    path('add_product/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('db/', views.total_in_db, name='db'),
]
