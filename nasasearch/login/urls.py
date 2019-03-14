from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'login'
urlpatterns = [
    path('register/', views.Register.as_view() , name='register'),
    path('login/', views.my_login , name='my_login'),
    path('logout/', views.my_logout, name ='my_logout'),
]