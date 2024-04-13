from django.urls import path
from listings import views


urlpatterns = [
    path('', views.home, name='home'),
    path('myaccount', views.myaccount, name='myaccount'),
]
