import json
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
import os
from task_manager.users.models import User

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)

FIXTURE_FILE = os.path.join(FIXTURE_DIR, 'user.json')
TEST_USER = json.load(open(FIXTURE_FILE))


class UpdateUser(TransactionTestCase):
    fixtures = ['db.json']
    username = TEST_USER.get('username')

    def test_update_without_login(self):
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': 1}
            ),
            TEST_USER
        )
        self.assertRedirects(response, reverse('login'))

    def test_redirect_after_update(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': user.id}
            ),
            TEST_USER
        )
        self.assertRedirects(response, reverse('users_list'))
        user = User.objects.get(pk=user.id)
        self.assertEqual(user.first_name, TEST_USER.get('first_name'))
        self.assertEqual(user.last_name, TEST_USER.get('last_name'))
        self.assertEqual(user.username, TEST_USER.get('username'))

    def test_modify_only_himself(self):
        self.assertEqual(User.objects.all().count(), 3)
        user1 = User.objects.all().first()
        testuser = User.objects.create_user(username='john', password='smith')
        self.assertEqual(User.objects.all().count(), 4)

        self.client.force_login(user=testuser)
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': user1.id}
            ),
            TEST_USER
        )
        self.assertRedirects(response, reverse('users_list'))
        user = User.objects.get(pk=user1.id)
        self.assertEqual(user1, user)
