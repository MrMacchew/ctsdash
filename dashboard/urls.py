from django.conf.urls import include, url

from .views import (
            HomePageView,
            AuthenticatedUserRoomList,
            RoomView,
            TicketView,
            CreateTicketView,
            AllRoomView,
            BuildingRooms,
            BuildingRoomListView,
            close_ticket
            )

action_patterns = [
    # This will probably always be fuction based views
    url(r'^close/(?P<ticket_id>[0-9]+)/$', close_ticket, name="ticket-close"),

]

all_patterns = [
    url(r'rooms/$', AllRoomView.as_view())
    # url(r'tickets/$', AllRoomView.as_view())
]

urlpatterns = [

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^rooms/$', AuthenticatedUserRoomList.as_view(), name='my-room-list'),
    url(r'^rooms/(?P<pk>\d+)$', RoomView.as_view(), name='room'),

    url(r'^building/(?P<pk>\d+)$', BuildingRoomListView.as_view(), name="building-rooms"),

    url(r'^tickets/(?P<pk>\d+)$', TicketView.as_view(), name='ticket'),
    url(r'^tickets/create$', CreateTicketView.as_view(), name='ticket-create'),


    # Extended Patterns
    url(r'^all/', include(all_patterns, namespace='all')),
    url(r'^actions/', include(action_patterns, namespace='actions')),

]


