from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Room


class HomePageView(TemplateView):
    template_name = 'home.html'


class AuthenticatedUserRoomList(ListView):
    template_name = 'rooms.html'

    def get_queryset(self):
        rooms = Room.objects.prefetch_related('user')
        return rooms.filter(user=self.request.user)



class RoomView(DetailView):
    template_name = 'room.html'
    model = Room
