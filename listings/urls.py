from django.urls import path
from listings import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('my_listings/', views.my_listings, name='my_listings'),
    path('create/', views.create_listing, name='create_listing'),
    path('listings/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('listings/<int:pk>/update/', views.update_listing, name='update_listing'),
    path('listings/<int:pk>/delete/', views.delete_listing, name='delete_listing'),
    path('listings/category/<int:category_id>/', views.category_page, name='category_page'),
    path('listings/pedal/<int:pedal_id>/', views.pedal_detail, name='pedal_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
