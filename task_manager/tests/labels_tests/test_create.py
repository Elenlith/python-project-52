from task_manager.users.models import User
from task_manager.labels.models import Label
from django.urls import reverse_lazy as reverse
from django.test import TestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class CreateLabel(TestCase):
    fixtures = [
        'db_labels.json',
        'db.json',
    ]

    def test_create_without_login(self):
        response = self.client.get(reverse('label_create'))
        self.assertEqual(response.status_code, 302)

    def test_create_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Label.objects.all().count(), 3)
        response = self.client.post(
            reverse('label_create'),
            {'name': 'test'}
        )
        self.assertEqual(Label.objects.all().count(), 4)
