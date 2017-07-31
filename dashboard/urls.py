from django.conf.urls import include, url

from .views import (
            HomePageView,
            RoomView,
            TicketView,
            CreateTicketView,
            RoomListView,
            BuildingRoomListView,
            TicketListView,
            close_ticket,
            open_ticket,
            RoomListView
            )

action_patterns = [
    # This will probably always be fuction based views
    url(r'^close/(?P<ticket_id>[0-9]+)/$', close_ticket, name="ticket-close"),
    url(r'^open/(?P<ticket_id>[0-9]+)/$', open_ticket, name="ticket-open"),

]

all_patterns = [
    url(r'rooms/$', RoomListView.as_view())
    # url(r'tickets/$', AllRoomView.as_view())
]

urlpatterns = [
    url(r'^building/(?P<pk>\d+)$', BuildingRoomListView.as_view(), name="building-rooms"),

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^rooms/(?P<pk>\d+)$', RoomView.as_view(), name='room'),

    url(r'^issues/(?P<pk>\d+)$', TicketView.as_view(), name='ticket'),
    url(r'^issues/$', TicketListView.as_view(), name='ticket-list'),
    url(r'^issues/create$', CreateTicketView.as_view(), name='ticket-create'),

    # Extended Patterns
    url(r'^all/', include(all_patterns, namespace='all')),
    url(r'^actions/', include(action_patterns, namespace='actions')),

]


