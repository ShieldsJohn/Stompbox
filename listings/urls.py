from django.urls import path
from listings import views


urlpatterns = [
    path('myaccount', views.myaccount, name='myaccount'),
]
