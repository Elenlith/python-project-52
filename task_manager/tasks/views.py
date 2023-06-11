from django.urls import reverse_lazy
from django.views.generic import CreateView,\
    UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.filters import TaskFilter
from django_filters.views import FilterView


# Create your views here.
class TasksListView(AuthRequiredMixin, FilterView):
    template_name = 'tasks/list.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks_list'


class TaskDetailsView(AuthRequiredMixin, DetailView):
    template_name = 'tasks/details.html'
    model = Task
    context_object_name = 'task'


class TaskCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        """
        Set current user as the task's author.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully changed')


class TaskDeleteView(AuthRequiredMixin, AuthorDeletionMixin,
                     SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully deleted')
    permission_denied_message = _('The task can be deleted only by its author')
    permission_denied_url = reverse_lazy('tasks_list')
