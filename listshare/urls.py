from django.contrib import admin
from django.urls import path
from django.urls import re_path
from lists import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    re_path('lists/(\d+)/', views.list_detail, name='list_detail'),
]
