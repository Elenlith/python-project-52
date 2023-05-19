from django.test import SimpleTestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class SimpleTest(SimpleTestCase):

    def test_open_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
