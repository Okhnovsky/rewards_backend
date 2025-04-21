from datetime import datetime

from celery import shared_task

from .models import RewardLog, SheduledReward


@shared_task
def add_reward(reward_id):
    reward = SheduledReward.objects.get(id=reward_id)
    user = reward.user
    user.coins += reward.amount
    user.save()
    RewardLog.objects.create(
        user=user, amount=reward.amount, given_at=datetime.now())
