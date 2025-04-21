from django.utils import timezone

from django.core.exceptions import ValidationError


def validate_execute_date(date):
    if date < timezone.now():
        raise ValidationError(
            "Execute time must be greater or equal than datetime.now()",
            params={"date": date},
        )
