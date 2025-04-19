from rest_framework.routers import DefaultRouter

from marketplace.mentors.views import MentorViewSet

router = DefaultRouter()
router.register("", MentorViewSet, basename="mentors")

urlpatterns = router.urls
