"""logoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from core.views import indexcore
from likes.views import indexlikes
from registration.views import indexregistration
from blogtxt.views import indextxt
from post.views import post_show
from categories.views import categories_show

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', indexcore),
    url(r'^likes/$', indexlikes),
    url(r'^registration/$', indexregistration),
    url(r'^blogtxt/$', indextxt),
    url(r'post/(\d+)/$', post_show),
    url(r'categories/$', categories_show)
]
