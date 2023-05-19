from task_manager.users.models import User
from task_manager.labels.models import Label
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase, modify_settings


modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)

class DeleteLabelWithTask(TransactionTestCase):
    fixtures = ['db_task_with_label.json']

    def test_delete_with_task_bound(self):
        label = Label.objects.all().first()
        user = User.objects.all().first()
        self.assertEqual(Label.objects.all().count(), 1)
        self.client.force_login(user=user)
        self.client.get(reverse('label_delete',
                                kwargs={'pk': label.id}))
        self.assertEqual(Label.objects.all().count(), 1)
