from django.urls import reverse_lazy as reverse
from django.test import TestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class SimpleTest(TestCase):

    def test_page_contains_links(self):
        list_links = [
            'users_list',
            'user_add',
            'login',
        ]
        response = self.client.get('/')
        for path in map(reverse, list_links):
            self.assertContains(response, path)

    def test_userlist_access_without_login(self):
        response = self.client.get(reverse('users_list'))
        self.assertEqual(response.status_code, 200)
