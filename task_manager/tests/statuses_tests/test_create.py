from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.urls import reverse_lazy as reverse
from django.test import TestCase


class CreateStatus(TestCase):
    fixtures = [
        'db_status.json',
        'db.json',
    ]

    def test_create_without_login(self):
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 302)

    def test_create_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        statuses = Status.objects.all()
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(statuses), 3)
        response = self.client.post(
            reverse('status_create'),
            {'name': 'test'}
        )
        statuses2 = Status.objects.all()
        self.assertEqual(len(statuses2), 4)
        status_added = statuses2[3]
        self.assertEqual(status_added.name, 'test')
