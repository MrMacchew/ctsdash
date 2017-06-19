from django.conf.urls import include, url
from .views import SignUpView, LoginView, LogOutView

urlpatterns = [
    url(r'^register/', SignUpView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogOutView.as_view(), name='logout'),
]
