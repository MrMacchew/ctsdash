from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Room
# Create your views here.


class RoomListView(ListView):
    models = Room


# class UserListView()

# class RoomPerUserListView(ListView):


# Via Django Rest Framework or a simple json view (protrectoed)

# class APIView For Numer of Rooms not Working
