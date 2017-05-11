#include 扩展urls到各站点
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^blog/',views.index),


]
