from task_manager.users.models import User
from django.urls import reverse_lazy as reverse
from django.test import TestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class TestFilter(TestCase):
    fixtures = [
        'db.json',
        'db_status.json',
        'db_tasks.json',
        'db_labels.json'
    ]

    def test_filter_by_status(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        self.client.get(reverse('tasks_list'))
        result = self.client.get(reverse('tasks_list'), {'status': '1'})
        self.assertContains(result, 'Task 1')
        self.assertNotContains(result, 'Task 2')
        self.assertContains(result, 'Task 3')

    def test_filter_by_executor(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        self.client.get(reverse('tasks_list'))
        result = self.client.get(reverse('tasks_list'), {'executor': '2'})
        self.assertContains(result, 'Task 1')
        self.assertNotContains(result, 'Task 2')
        self.assertNotContains(result, 'Task 3')

    def test_filter_by_label(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        self.client.get(reverse('tasks_list'))
        result = self.client.get(reverse('tasks_list'), {'labels': '2'})
        self.assertContains(result, 'Task 1')
        self.assertContains(result, 'Task 2')
        self.assertNotContains(result, 'Task 3')
