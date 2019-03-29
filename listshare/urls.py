from django.contrib import admin
from django.urls import path, re_path, include
from lists import views
from  django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    re_path('lists/(\d+)/', views.list_detail, name='list_detail'),
    re_path('edit/(\d+)/', views.edit_list, name='edit_list'),
]
