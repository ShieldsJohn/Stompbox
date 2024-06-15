from django.urls import path
from users import views
from .models import Profile


urlpatterns = [
    path('users/', views.myaccount, name='myaccount'),
    path('view_myaccount/', views.view_myaccount, name='view_myaccount'),
    path('profile_form/', views.profile_form, name='profile_form'),
    path(
        'profile_form_success/',
        views.profile_form_success,
        name='profile_form_success'),
    path(
        'delete_account_confirmation/',
        views.delete_account_confirmation,
        name='delete_account_confirmation'),
    path('account_deleted/', views.account_deleted, name='account_deleted'),
    path(
        'contact_seller/<int:listing_id>/',
        views.contact_seller,
        name='contact_seller'),
]
