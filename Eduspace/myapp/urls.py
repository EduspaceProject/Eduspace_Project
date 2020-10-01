from django.contrib import admin
from django.urls import path,include
from .views import home,login,register
urlpatterns = [
    path('',home),
    path('login/',login),
    path('register/',register)

]
