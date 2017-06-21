from django.conf.urls import include, url

from .views import (
            HomePageView,
            AuthenticatedUserRoomList,
            RoomView,
            TicketView,
            AllRoomView,
            close_ticket
            )

all_patterns = [
    url(r'rooms/$', AllRoomView.as_view())
    # url(r'^reports/$', credit_views.report),
    # url(r'^reports/(?P<id>[0-9]+)/$', credit_views.report),
    # url(r'^charge/$', credit_views.charge),
]

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^rooms/$', AuthenticatedUserRoomList.as_view(), name='my-room-list'),
    url(r'^rooms/(?P<pk>\d+)$', RoomView.as_view(), name='room'),
    url(r'^tickets/(?P<pk>\d+)$', TicketView.as_view(), name='ticket'),
    url(r'^close/(?P<ticket_id>[0-9]+)/$', close_ticket, name="ticket-close"),
    url(r'^all/', include(all_patterns, namespace='all')),

]


