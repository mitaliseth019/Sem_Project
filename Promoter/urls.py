from django.contrib import admin
from django.urls import include ,path
from . import views

urlpatterns = [
    path('', views.index, name = "home" ),
    #path('',include('Promoter.urls')),
    path('accounts/',include('allauth.urls')),
]
