from django.urls import path
from . import views, admin
from django.contrib import admin

app_name='main'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

]
