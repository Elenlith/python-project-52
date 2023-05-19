from task_manager.users.models import User
from task_manager.tasks.models import Task
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class DeleteTask(TransactionTestCase):
    fixtures = ['db_task.json']

    def test_delete_without_login(self):
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('task_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.all().count(), 0)
