from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('indexs/', views.indexs, name='video'),  # Use views.indexs, not views.indexs()
    path('indexs/', views.indexs, name='indexs'),
    # Add more paths as needed
]