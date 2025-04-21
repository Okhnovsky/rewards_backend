from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Расширенная модель пользователя.
    """

    coins = models.IntegerField(
        verbose_name="Монеты",
        default=0,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
