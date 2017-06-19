from django.shortcuts import render
from django.views import generic
from .models import Room

class HomePageView(generic.TemplateView):
    template_name = 'home.html'
