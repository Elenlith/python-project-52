from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class IndexView(TemplateView):
    template_name = "index.html"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')

    def form_valid(self, form):
        messages.info(self.request, _('You are logged in'))
        return super().form_valid(form)

    def form_invalid(self, form):
        login_failure_eng_text = 'Please enter correct username and password. '\
            'Both fields may be case sensitive'
        login_failure_text = _(login_failure_eng_text)
        messages.error(self.request, login_failure_text)
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    success_message = _('You are logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
