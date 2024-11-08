from django.urls import path
from goods import views, admin
from django.contrib import admin

app_name='goods'


urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),

]
