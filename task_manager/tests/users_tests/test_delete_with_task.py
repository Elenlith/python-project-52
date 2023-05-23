from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.users.models import User
from task_manager.tasks.models import Task


class Remove(TransactionTestCase):
    fixtures = ['db_task_two_users.json']

    def test_delete_with_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user.id}
            )
        )
        self.assertRedirects(response, reverse('users_list'))
        self.assertEqual(User.objects.all().count(), 2)

    def test_delete_after_modifying_task(self):
        user1 = User.objects.all().first()
        user2 = User.objects.all().last()
        task = Task.objects.all().first()
        self.assertEqual(Task.objects.all().count(), 1)
        task.author = user2
        task.executor = user2
        task.save()
        self.client.force_login(user=user1)
        self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user1.id}
            )
        )
        self.assertEqual(User.objects.all().count(), 1)
