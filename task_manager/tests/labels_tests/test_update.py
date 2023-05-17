from task_manager.users.models import User
from task_manager.labels.models import Label
from django.urls import reverse_lazy as reverse
from django.test import TestCase


class UpdateStatus(TestCase):
    fixtures = [
        'db_labels.json',
        'db.json',
    ]

    def test_update_without_login(self):
        response = self.client.get(reverse('label_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_update_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('label_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('label_update', kwargs={'pk': 1}),
            {'name': 'test'}
        )
        label = Label.objects.get(pk=1)
        self.assertEqual(label.name, 'test')
