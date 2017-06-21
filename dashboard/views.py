from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Room, Ticket
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

class HomePageView(TemplateView):
    template_name = 'home.html'


class AuthenticatedUserRoomList(LoginRequiredMixin, ListView):
    template_name = 'rooms.html'

    def get_queryset(self):
        rooms = Room.objects.prefetch_related('user')
        return rooms.filter(user=self.request.user)

class RoomView(LoginRequiredMixin, DetailView):
    template_name = 'room.html'
    model = Room

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs) # get the default context data
        print(self)
        context['tickets'] = Ticket.objects.filter(room=self.kwargs['pk'], complete=False) # add extra field to the context
        return context

class AllRoomView(LoginRequiredMixin, ListView):
    template_name = 'all/rooms.html'
    model = Room


class TicketView(LoginRequiredMixin, DetailView):
    template_name = 'ticket.html'
    model = Ticket


class AllTicketView(LoginRequiredMixin, ListView):
    template_name = 'tickets.html'
    model = Ticket


@login_required
def close_ticket(request, ticket_id):
    try:
        Ticket.objects.filter(id=ticket_id).update(complete=True)
    except Ticket.DoesNotExist:
        raise Http404("Poll does not exist")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

