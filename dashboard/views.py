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
    template_name= "list_room_by_floor.html"

    def get_queryset(self):
        return Room.objects.filter(building=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        context = super(BuildingRoomListView, self).get_context_data(**kwargs)
        return context


class RoomListView(ListView):
    template_name = 'list_room_by_building.html'

    def get_queryset(self):
        return Room.objects.all()


class RoomView(DetailView):
    template_name = 'detail_room.html'
    model = Room

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs) # get the default context data
        ticket_filter = Ticket.objects.filter(room=self.kwargs['pk'])
        context['tickets'] = Ticket.objects.filter(room=self.kwargs['pk'], complete=False) # add extra field to the context
        context['closed'] = ticket_filter.filter(complete=True)
        return context


class HomePageView(TemplateView):
    template_name = 'home.html'


    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['buildings'] = Building.objects.all()
        return context

class TicketListView(LoginRequiredMixin, ListView):
    template_name = 'list_ticket.html'

    def get_queryset(self):
        return Ticket.objects.filter(complete=False)


# Actions
@login_required
def close_ticket(request, ticket_id):
    try:
        # Not using signals because it does not trigger signals
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.complete = True
        ticket.save()

    except Ticket.DoesNotExist:
        raise Http404("ticket does not exist")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def open_ticket(request, ticket_id):
    try:
        # Not using signals because it does not trigger signals
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.complete = False
        ticket.save()
    except Ticket.DoesNotExist:
        raise Http404("ticket does not exist")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class CreateTicketView(CreateView):
    model = Ticket
    template_name= "create_ticket.html"
    form_class = TicketForm


# ======================= #



# REMOVE
class AuthenticatedUserRoomList(LoginRequiredMixin, ListView):
    template_name = 'rooms.html'

    def get_queryset(self):
        rooms = Room.objects.prefetch_related('user')
        return rooms.filter(user=self.request.user)


class TicketView(LoginRequiredMixin, DetailView):
    template_name = 'detaiL_ticket.html'
    model = Ticket




