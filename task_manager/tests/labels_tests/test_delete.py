from task_manager.users.models import User
from task_manager.labels.models import Label
from django.urls import reverse_lazy as reverse
from django.test import TestCase


class DeleteLabel(TestCase):
    fixtures = [
        'db_labels.json',
        'db.json',
    ]

    def test_delete_without_login(self):
        response = self.client.get(reverse('label_delete', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 302)

    def test_delete_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('label_delete', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('label_delete', kwargs={'pk': 3})
        )
        labels = Label.objects.all()
        self.assertEqual(len(labels), 2)
