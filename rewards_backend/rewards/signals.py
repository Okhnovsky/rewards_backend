from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import SheduledReward
from .tasks import add_reward


@receiver(post_save, sender=SheduledReward)
def execute_reward(sender, instance, created, **kwargs):
    if created:
        print(instance.id)
        add_reward.apply_async(args=[instance.id], eta=instance.execute_at)
