from task_manager.users.models import User
from django.urls import reverse_lazy as reverse
from django.test import TestCase


class List(TestCase):
    fixtures = [
        'db_labels.json',
        'db.json',
    ]

    def test_list_without_login(self):
        response = self.client.get(reverse('labels_list'))
        self.assertEqual(response.status_code, 302)

    def test_list_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('labels_list'))
        self.assertEqual(response.status_code, 200)
