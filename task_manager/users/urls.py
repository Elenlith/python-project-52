from django.urls import path
from task_manager.users.views import UsersListView, UserCreateView,\
    UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='user_add'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
