from rest_framework import routers

from vacancies.views import VacanciesViewSet


router = routers.DefaultRouter()
router.register("", VacanciesViewSet, basename="vacancies")
urlpatterns = router.urls