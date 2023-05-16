from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.urls import reverse_lazy as reverse
from django.test import TestCase


class UpdateStatus(TestCase):
    fixtures = [
        'db_status.json',
        'db.json',
    ]

    def test_update_open_without_login(self):
        response = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_update(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('status_update', kwargs={'pk': 1}),
            {'name': 'test'}
        )
        status = Status.objects.get(pk=1)
        self.assertEqual(status.name, 'test')
