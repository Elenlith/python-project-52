from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from .models import Status
from .forms import StatusForm

# Create your views here.
class StatusesListView(AuthRequiredMixin, ListView):
    template_name = 'statuses/list.html'
    model = Status
    context_object_name = 'statuses_list'
    extra_context = {
        'title': _('Statuses')
    }


class StatusCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status successfully created')
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }


class StatusUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status successfully changed')
    extra_context = {
        'title': _('Change status'),
        'button_text': _('Change'),
    }


class StatusDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                       SuccessMessageMixin, DeleteView):
    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status successfully deleted')
    protected_message = _('It is not possible to delete a status '
                          'because it is in use')
    protected_url = reverse_lazy('statuses_list')
    extra_context = {
        'title': _('Delete status'),
        'button_text': _('Yes, delete'),
    }
