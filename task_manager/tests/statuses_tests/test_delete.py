from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.urls import reverse_lazy as reverse
from django.test import TestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class DeleteStatus(TestCase):
    fixtures = [
        'db_status.json',
        'db.json',
    ]

    def test_delete_without_login(self):
        response = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('status_delete', kwargs={'pk': 1})
        )
        statuses = Status.objects.all()
        self.assertEqual(len(statuses), 2)
