from django.contrib import admin

from .models import SheduledReward, RewardLog


@admin.register(SheduledReward)
class SheduledRewardAdmin(admin.ModelAdmin):

    list_display = ("user", "amount", "execute_at",)


@admin.register(RewardLog)
class RewardLog(admin.ModelAdmin):

    list_display = ("user", "amount", "given_at",)
