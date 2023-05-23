from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.users.models import User


class DeleteUser(TransactionTestCase):
    fixtures = ['db.json']

    def test_delete_without_login(self):
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': 1}
            )
        )
        self.assertRedirects(response, reverse('login'))
        users = User.objects.all().count()
        self.assertEqual(users, 3)

    def test_delete_only_himself(self):
        user1 = User.objects.all().first()
        user2 = User.objects.all().last()
        self.client.force_login(user=user2)
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user1.id}
            )
        )
        self.assertRedirects(response, reverse('users_list'))
        self.assertIn(user1, User.objects.all())
        self.assertEqual(User.objects.all().count(), 3)

    def test_delete(self):
        user1 = User.objects.all().first()
        self.client.force_login(user=user1)
        response = self.client.post(
             reverse(
                 'user_delete',
                 kwargs={'pk': user1.id}
             )
        )
        self.assertRedirects(response, reverse('users_list'))
        self.assertEqual(User.objects.all().count(), 2)
        self.assertNotIn('unclefedor', User.objects.all())
