from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm


# Create your views here.
class LabelsListView(AuthRequiredMixin, ListView):
    template_name = 'labels/list.html'
    model = Label
    context_object_name = 'labels_list'


class LabelCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')
    success_message = _('Label successfully created')
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')
    success_message = _('Label successfully changed')
    extra_context = {
        'title': _('Change label'),
        'button_text': _('Change'),
    }


class LabelDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                      SuccessMessageMixin, DeleteView):
    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels_list')
    success_message = _('Label successfully deleted')
    deny_delete_message = _('It is not possible to delete a label '
                            'because it is in use')
    deny_delete_url = reverse_lazy('labels_list')
