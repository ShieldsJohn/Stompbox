from django.urls import path
from listings import views

urlpatterns = [
    path('my_listings/', views.my_listings, name='my_listings'),
    path('create/', views.create_listing, name='create_listing'),
    path('listings/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('listings/<int:pk>/update/', views.update_listing, name='update_listing'),
    path('listings/<int:pk>/delete/', views.delete_listing, name='delete_listing'),
]
