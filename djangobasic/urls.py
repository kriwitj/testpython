"""djangobasic URL Configuration

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
from django.urls import path, re_path
from blogs import views

from django.conf import settings
#from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('page1',views.page1),
    path('createForm',views.createForm),
    path('addForm',views.addUser),
    path('loginForm',views.loginForm),
    path('login',views.login),
    path('logout',views.logout),
    path('register_item',views.register_item),
    path('addItem',views.addItem),
    path('edit_item',views.edit_item),
    path('load_item',views.load_item),
    #path('register_act',views.register_act),
    path('add_act',views.add_act),
    path('edit_act',views.edit_act),
    path('home_act',views.home_act),
    path('register_act',views.register_view),
    path('home',views.home_view),


    #image
    path('image_upload', views.hotel_image_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('hotel_images', views.display_hotel_images, name = 'hotel_images')
]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    #urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
