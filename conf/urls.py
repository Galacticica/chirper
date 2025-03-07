"""
File: urls.py
Author: Reagan Zierke, Aleksa Chambers, Caden Korell
Date: 3/6/2025
Description: The urls for the project.
"""


from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('chirps.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/'), name='profile'),
]
