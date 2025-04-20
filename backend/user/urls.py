from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserBioViewSet

router = DefaultRouter()
router.register(r'', UserBioViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]