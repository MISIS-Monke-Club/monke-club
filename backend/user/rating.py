from django.db.models import Count
from .models import UserRatingActivity

MAX_ACTIVITIES = 7

def add_user_activity(user, activity_type, once=True):
    if once and UserRatingActivity.objects.filter(user=user, activity_type=activity_type).exists():
        return

    UserRatingActivity.objects.create(user=user, activity_type=activity_type)

    total = UserRatingActivity.objects.filter(user=user).count()
    rating = round(min((total / MAX_ACTIVITIES) * 5.0, 5.0), 1)

    if hasattr(user, "bio"):
        user.bio.rating = rating
        user.bio.save(update_fields=["rating"])