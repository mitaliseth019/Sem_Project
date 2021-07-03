
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
    path("accounts/login/?next=/findcreator/",views.findcreator,name="findcreator"),

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


urlpatterns+=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
