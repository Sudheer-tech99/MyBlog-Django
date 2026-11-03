"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.views.generic import RedirectView
from django.urls import path
from app_1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home,name='Home'),
    path('', RedirectView.as_view(url='/home/', permanent=False), name='Base'),
    path('Allnewpost/',Allnewpost,name="Allnewpost"),
    path('Allcategories/',Allcategories,name='Allcategories'),
    path('Addpost/', Addpost, name='Addpost'),
    path('Blogdetails/<int:post_id>/', Blogdetails, name='Blogdetails'),
    path('Deletepost/<int:post_id>/', Deletepost, name='Deletepost'),
    path('Cetagory/<int:category_id>/', Cetagory, name='Cetagory'),
    path('Login/',Login,name='Login'),
    path('Register/',Register,name='Register'),
    ]
