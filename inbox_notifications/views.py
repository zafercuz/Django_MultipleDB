from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import ListView, DetailView
from notifications.models import Notification
from notifications.utils import slug2id


class InboxNotificationListView(ListView):
    template_name = 'notification-inbox.html'
    model = Notification
    context_object_name = 'notifications'
    ordering = ['-timestamp']

    def get_queryset(self):
        user = User.objects.get(pk=self.request.user.id)
        qs = user.notifications.exclude(deleted=True)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notification Inbox'
        return context


class InboxNotificationTrashListView(ListView):
    template_name = 'notification-trash.html'
    model = Notification
    context_object_name = 'notifications'
    ordering = ['-timestamp']

    def get_queryset(self):
        user = User.objects.get(pk=self.request.user.id)
        print()
        qs = user.notifications.exclude(deleted=False)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notification Inbox'
        return context


def InboxNotificationDetailView(request, slug=None):
    template_name = 'notification-detail.html'
    notification_id = slug2id(slug)
    notification = get_object_or_404(Notification, recipient=request.user, id=notification_id)
    notification.mark_as_read()

    return render(request, template_name, {'notification': notification, 'title': 'Notification Detail'})


def inbox_notification_move_to_trash(request, slug=None):
    notification_id = slug2id(slug)
    notification = get_object_or_404(Notification, recipient=request.user, id=notification_id)
    print(notification)
    print(notification.deleted)
    notification.deleted = True
    notification.save()
    print(notification.deleted)
    success_message = "Successfully moved notification to trash"
    messages.success(request, success_message)

    return HttpResponseRedirect(reverse('testinbox'))
