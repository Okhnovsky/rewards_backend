from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import RetrieveProfile, ListGivenRewards, CreateReward


app_name = "api"


urlpatterns = [
    path('token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/', RetrieveProfile.as_view(), name="profile"),
    path('rewards/', ListGivenRewards.as_view(), name="given_rewards"),
    path('rewards/request/', CreateReward.as_view(), name="create_reward"),
]
