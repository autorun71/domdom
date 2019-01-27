from django.contrib import admin
from django.urls import path, re_path
from domdom.apps.domapp import views

#     re_path(r'post/(?P<index>.+)/$', views.posts),
urlpatterns = [
    path('', views.index),
    path('catalog/', views.catalog),
    path('catalog/', views.catalog),
    re_path(r'catalog/(?P<index>.+)/$', views.alt_url),
    path('robots.txt', views.robots),


]
