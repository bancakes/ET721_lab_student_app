from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('view-images/', views.view_images, name='view_images'),
]
