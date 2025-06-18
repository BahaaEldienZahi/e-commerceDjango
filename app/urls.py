from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.my_logout, name='logout'),
]
