"""hostelbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("index/",views.index,name="index"),
    path("hostel/",views.hostel,name="hostel"),
    path("registerhostel/",views.registerhostel,name='registerhostel'),
    path("collecthostel/",views.collecthostel,name="collecthostel"),
    path("registeryourhostel/",views.registeryourhostel,name="registeryourhostel"),
    path("login/",views.login,name="login"),
    path("loginyourself/",views.loginyourself,name="loginyourself"),
    path("addroom/",views.addroom,name="addroom"),
    path("showDetail/<hostel_id>",views.showDetail,name="showDetail"),
    path("showRooms/<hostel_id>",views.showRooms,name="showRooms"),
    path("tenantPage/<room_id>",views.tenantPage,name="tenantPage"),
    path("registertenant/<room_id>",views.registerTenant,name="registertenant"),
    path("abouttefin/",views.abouttefin,name="abouttefin"),
    path("abouttenentroom/",views.abouttenentroom,name="abouttenentroom"),
    path("orderTefin/<tenant_id>",views.orderTefin,name="orderTefin"),



]