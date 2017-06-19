from django.conf.urls import include, url
from .views import HomePageView, AuthenticatedUserRoomList, RoomView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^rooms/$', AuthenticatedUserRoomList.as_view(), name='my-room-list'),
    url(r'^rooms/(?P<pk>\d+)$', RoomView.as_view(), name='room'),

]
