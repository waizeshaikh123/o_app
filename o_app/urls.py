
from django.contrib import admin
from django.urls import path
from o_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('service/',views.service,name='service'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact')
]
