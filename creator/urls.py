from django.contrib import admin
from django.urls import include ,path
from . import views

urlpatterns = [
    path('creator/signin/', views.loginPage, name = "CreatorSignin" ),
    path('creator/signup/', views.registerPage, name = "CreatorSignup" ),
    #path('accounts/',include('allauth.urls')),
    path('creator/logout/', views.logoutUser, name = "Creatorlogout" ),
   
    #path('creator/form/', views.creatorprofile, name = "CreatorProfile" ),
    path('creator/customer/<str:pk_test>/', views.customer, name="customer"),

    #path('creator/creator_profile/',views.profile,name = "profile"),
   
]
