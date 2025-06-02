from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
]