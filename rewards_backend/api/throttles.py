from rest_framework.throttling import UserRateThrottle


class RequestRewardThrottle(UserRateThrottle):
    """
    Ограничивает количество запросов до 1 раза в сутки.
    """

    def allow_request(self, request, view):
        self.rate = '1/day'
        self.num_requests, self.duration = self.parse_rate(self.rate)
        return super().allow_request(request, view)
