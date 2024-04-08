from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('', views.myaccount, name='myaccount'),
]