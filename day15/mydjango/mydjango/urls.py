"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#include 扩展urls到各站点
from django.conf.urls import url,include
from django.contrib import admin
#1.导入blog中的views
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #所有到^blog的访问,到blog下的urls中查找

    url(r'^login/',views.login,name='LOGIN'),
    url(r'^book/',views.book),
    url(r'^addbook/',views.addbook),
    url(r'^delbook/',views.delbook),
    url(r'^editbook/',views.editbook),
    url(r'^blog/',include('blog.urls')),
]
