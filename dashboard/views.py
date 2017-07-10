from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Room, Ticket, Building
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .forms import TicketForm



class BuildingRoomListView(ListView):
    template_name= "building_rooms.html"

    def get_queryset(self):
        return Room.objects.filter(building=self.kwargs['pk'])



class BuildingRooms(ListView):
    template_name = 'rooms.html'

    def get_queryset(self):
        return Room.objects.filter(building=self.kwargs['pk'])


class HomePageView(TemplateView):
    template_name = 'home.html'


    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['buildings'] = Building.objects.all()
        return context


class CreateTicketView(CreateView):
    model = Ticket
    template_name= "create_ticket.html"
    form_class = TicketForm


class AuthenticatedUserRoomList(LoginRequiredMixin, ListView):
    template_name = 'rooms.html'

    def get_queryset(self):
        rooms = Room.objects.prefetch_related('user')
        return rooms.filter(user=self.request.user)

class AllRoomView(LoginRequiredMixin, ListView):
    template_name = 'all/rooms.html'
    model = Room

class RoomView(LoginRequiredMixin, DetailView):
    template_name = 'room.html'
    model = Room

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs) # get the default context data
        context['tickets'] = Ticket.objects.filter(room=self.kwargs['pk'], complete=False) # add extra field to the context
        return context


class TicketView(LoginRequiredMixin, DetailView):
    template_name = 'ticket.html'
    model = Ticket

class AllTicketView(LoginRequiredMixin, ListView):
    template_name = 'tickets.html'
    model = Ticket


# Actions

@login_required
def close_ticket(request, ticket_id):
    try:
        Ticket.objects.filter(id=ticket_id).update(complete=True)
    except Ticket.DoesNotExist:
        raise Http404("ticket does not exist")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

