from django.shortcuts import render
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from .models import User


# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = 'users'
    extra_context = {
        'title': _('Users')
    }
