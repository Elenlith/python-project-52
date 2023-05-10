from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin,\
    UserPermissionMixin, DeleteProtectionMixin


# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = 'users_list'
    extra_context = {
        'title': _('Users')
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    extra_context = {
        'title': _('Create user'),
        'button_text': _('Register'),
    }
    success_message = _('User is successfully registered')


class UserUpdateView(AuthRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')
    permission_url = reverse_lazy('users')
    extra_context = {
        'title': _('Update user'),
        'button_text': _('Update'),
    }
    success_message = _('User is successfully updated')
    permission_message = _('You have no rights to change another user.')


class UserDeleteView(AuthRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully deleted')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }
