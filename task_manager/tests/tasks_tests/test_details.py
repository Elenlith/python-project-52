from task_manager.users.models import User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.tasks.models import Task, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class SpecifyTask(TransactionTestCase):
    fixtures = ['db_task.json']

    def test_details_without_login(self):
        response = self.client.get(reverse(
            'task_details', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_details_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        self.assertEqual(Task.objects.all().count(), 1)
        task = Task.objects.all().first()
        response = self.client.get(reverse(
            'task_details', args=[task.id]))
        self.assertEqual(response.status_code, 200)
