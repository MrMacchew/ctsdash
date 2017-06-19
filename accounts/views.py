from django.views import generic
from django.contrib.auth import get_user_model
from .forms import RegistrationForm, LoginForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin


class SignUpView(AnonymousRequiredMixin, generic.CreateView):
    authenticated_redirect_url = "/"
    form_class = RegistrationForm
    model = get_user_model()
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class LoginView(AnonymousRequiredMixin, generic.FormView):
    authenticated_redirect_url = "/"
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'

    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogOutView(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('home')
    login_url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
