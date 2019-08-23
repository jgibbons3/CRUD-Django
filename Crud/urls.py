from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #path('send/', views.usuarioList, name='index'),
    path('add/', views.usuarioCreate, name='add'),
    path('usuarioDelete/<id>/', views.usuarioDelete, name='delete'),
    path('usuarioUpdate/<id>/', views.usuarioUpdate, name='update'),
    path('', views.usuarioList, name='index'),
    
]