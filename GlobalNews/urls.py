"""GlobalNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="indexpage"),
    path('content/',views.content,name="contentpage"),
    path('fullnews/',views.fullnews,name="fullnewspage"),
    path('search/', views.search, name="searchpage"),
    path('contact/', views.contact, name="contactpage"),
    path('about/', views.about, name="aboutpage"),
    path('privacy/', views.privacy, name="privacypage"),
    path('disclaimer/', views.disclaimer, name="disclaimerpage"),
    path('terms/', views.terms, name="termspage"),
    path('new/', views.new, name="newpage"),
    path('new2/', views.new2, name="new2page"),
    path('list/', views.list, name="listpage"),
    path("login/",views.login,name="loginpage"),
    path("logout/",views.logout,name="logoutpage"),
    path("register/",views.register,name="registerpage"),
    path("comment/",views.comment,name="commentpage"),
    path("tag/",views.tag,name="tagpage"),
    path("sidetag/",views.sidetag,name="sidetagpage"),

 
  
  











]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)