from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from index.models import Post


@receiver(post_save, sender=Post)
def post_blog_notification(sender, instance, **kwargs):
    """
    actor, recipient, verb, action_object, target, level, description, public, timestamp, **kwargs
    """
    notify.send(instance.author, recipient=instance.author, verb='You have created', description=instance)
