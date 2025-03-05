from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Chirp

class HomeView(ListView):
    model = Chirp
    template_name = "chirps/homepage.html"
    context_object_name = "chirps"
    ordering = ["-created_at"]


