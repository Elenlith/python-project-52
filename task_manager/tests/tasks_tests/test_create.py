from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from django.urls import reverse_lazy as reverse
from django.test import TestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class CreateTask(TestCase):
    fixtures = ['db_task.json']

    def test_create_open_without_login(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 302)

    def test_create_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        status = Status.objects.all().first()
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 1)
        response = self.client.post(
            reverse('task_create'),
            {'name': 'test task',
             'author': user.id,
             'status': status.id,
             'executor': user.id
             }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.all().count(), 2)
