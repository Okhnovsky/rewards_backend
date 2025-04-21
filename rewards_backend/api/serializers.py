from rest_framework import serializers

from users.models import CustomUser
from rewards.models import RewardLog


class ProfileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных профиля.
    """

    class Meta:
        model = CustomUser
        fields = ("username", "email", "coins",)


class RewardLogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для выданных наград.
    """

    class Meta:
        model = RewardLog
        fields = ("amount", "given_at",)


class RewardSerializer(serializers.Serializer):
    """
    Сериализатор для запроса награды.
    """

    amount = serializers.IntegerField()

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Incorrect amount value.")
        return value
