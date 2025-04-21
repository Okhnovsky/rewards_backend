import uuid

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from .validators import validate_execute_date


class SheduledReward(models.Model):
    """
    Модель запланированной награды.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        related_name="sheduled_rewards",
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        "Количество монет",
        validators=[MinValueValidator(1)],
    )
    execute_at = models.DateTimeField(
        "Запланированное время выполнения",
        validators=[validate_execute_date],
    )

    class Meta:
        verbose_name = "Запланированная награда"
        verbose_name_plural = "Запланированные награды"
        indexes = [
            models.Index(fields=["id"]),
        ]

    def __str__(self):
        return f"Награда для {self.user.username}"


class RewardLog(models.Model):
    """
    Модель лога запланированной награды.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        related_name="reward_logs",
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        "Количество монет",
    )
    given_at = models.DateTimeField(
        "Награда зачислена в",
    )

    class Meta:
        verbose_name = "Лог награды"
        verbose_name_plural = "Логи наград"
        indexes = [
            models.Index(fields=["id"]),
        ]

    def __str__(self):
        return f"Награда для {self.user.username}"
