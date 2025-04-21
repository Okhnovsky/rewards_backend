from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from drf_spectacular.utils import extend_schema

from users.models import CustomUser
from rewards.models import RewardLog, SheduledReward

from .serializers import (
    ProfileSerializer, RewardLogSerializer, RewardSerializer,
)
from .throttles import RequestRewardThrottle


class RetrieveProfile(APIView):
    """
    Получение информации о себе.
    """

    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses=ProfileSerializer,
    )
    def get(self, request):
        user = CustomUser.objects.get(username=self.request.user.username)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class ListGivenRewards(generics.ListAPIView):
    """
    Список выданных наград для запрашивающего пользователя.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = RewardLogSerializer

    def get_queryset(self):
        return RewardLog.objects.filter(user=self.request.user)


class CreateReward(APIView):
    """
    Создает награду спустя 5 минут после запроса пользователя.
    """

    permission_classes = [IsAuthenticated]
    throttle_classes = [RequestRewardThrottle]

    @extend_schema(
        request=RewardSerializer,
    )
    def post(self, request):
        serializer = RewardSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(username=self.request.user.username)
            execute_at = timezone.now() + timezone.timedelta(minutes=5)
            SheduledReward.objects.create(
                user=user,
                amount=serializer.data["amount"],
                execute_at=execute_at,
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
