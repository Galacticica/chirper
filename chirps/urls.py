"""
File: urls.py
Author: Reagan Zierke
Date: 3/6/2025
Description: Creates urls for the home page and each individual chirp.
"""



from django.urls import path
from .views import HomeView, ChirpView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('chirp/<int:chirp_id>/', ChirpView.as_view(), name='chirp_detail'),
]