"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("about/",views.aboutpage,name="about"),
    path("faq/",views.faqpage,name="faq"),
    path("contact/",views.contactpage,name="contact"),
    path("signup/",views.register,name="reg"),
    path("check_user/",views.check_user,name="check_user"),
    path("user_login",views.user_login,name="user_login"),
    path('<str:username>/', views.profile, name='profile'),
    #path("company/",views.sendcompany,name="sendcompany"),
    #path("job/",views.job,name="job"),
    path("cust_dashboard",views.cust_dashboard,name="cust_dashboard"),
    path("inbox",views.inbox,name="inbox"),
    path("request",views.request,name="request"),
    path("seller_dashboard/",views.seller_dashboard,name="seller_dashboard"),
    path("user_logout/hypeit",views.user_logout,name="user_logout"),
    path("edit_profile/hypeit",views.edit_profile,name="edit_profile"),
    path("change_password/",views.change_password,name="change_password"),
    path('search/hypeit', views.search, name="search"),
    path("forgotpass",views.forgotpass, name="forgotpass"),

   
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
