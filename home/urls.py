from django.urls import include,path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("about/", views.about, name="AboutUs"),
    path('accounts/',include('allauth.urls')),
    path("contact/", views.contact, name="ContactUs"),
    

]