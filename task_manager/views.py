from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {'title': _('Task manager')}


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')
    extra_context = {
        'title': _('Login'),
        'button_text': _('Enter'),
    }
    
    def form_valid(self, form):
        messages.info(self.request, _('You are logged in'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Please enter correct username and password. Both fields may be case sensitive'))
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    success_message = _('You are logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
