from task_manager.users.models import User
from task_manager.tasks.models import Task
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase


class ListTasks(TransactionTestCase):
    fixtures = ['db_task.json']

    def test_list_without_login(self):
        response = self.client.get(reverse('tasks_list'))
        self.assertEqual(response.status_code, 302)

    def test_list_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('tasks_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 1)
        task = Task.objects.all().first()
        task.delete()
        self.assertEqual(Task.objects.all().count(), 0)
        self.assertEqual(response.status_code, 200)
