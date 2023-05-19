from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class UpdateTask(TransactionTestCase):
    fixtures = ['db_task.json']

    def test_update_without_login(self):
        response = self.client.get(reverse('task_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('task_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_update_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('task_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        task = Task.objects.all().first()
        status = Status.objects.all().first()
        user2 = User.objects.create_user(username='test', password='testpass')
        task2 = {
            'name': 'test_task',
            'status': status.id,
            'executor': user2.id,
        }
        response = self.client.post(
            reverse('task_update', kwargs={'pk': task.id}),
            task2
        )

        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(pk=task.id)
        self.assertEqual(task.name, task2['name'])
        self.assertEqual(task.executor_id, task2['executor'])
