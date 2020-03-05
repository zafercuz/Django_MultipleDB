from django.urls import path
from .views import InboxNotificationListView, InboxNotificationDetailView, inbox_notification_move_to_trash, \
    InboxNotificationTrashListView

urlpatterns = [
    path('', InboxNotificationListView.as_view(), name='testinbox'),
    path('notification/trash', InboxNotificationTrashListView.as_view(), name='notification-trash'),
    path('notification/<slug:slug>', InboxNotificationDetailView, name='notification-detail'),
    path('notification/<slug:slug>/trash', inbox_notification_move_to_trash, name='notification-move-to-trash'),
]
