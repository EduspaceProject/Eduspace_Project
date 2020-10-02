from django.contrib import admin
from django.urls import path,include
from .views.login import Login
from .views.register import Register
from .views.home import home
urlpatterns = [
    path('',home,name='homepage'),
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register')

]
