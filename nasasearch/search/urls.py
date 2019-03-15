from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'search'
urlpatterns = [
    path('', views.search , name='search'),
 ]