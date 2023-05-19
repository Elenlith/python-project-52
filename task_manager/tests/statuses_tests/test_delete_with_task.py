from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class DeleteStutusWithTask(TransactionTestCase):
    fixtures = ['db_task_two_users.json']

    def test_delete_with_task(self):
        status = Status.objects.all().first()
        user = User.objects.all().first()
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.force_login(user=user)
        self.client.get(reverse('status_delete',
                                kwargs={'pk': status.id}))
        self.assertEqual(Status.objects.all().count(), 1)
