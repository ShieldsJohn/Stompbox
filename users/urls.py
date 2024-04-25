from django.urls import path
from users import views


urlpatterns = [
    path('myaccount', views.myaccount, name='myaccount'),
]
