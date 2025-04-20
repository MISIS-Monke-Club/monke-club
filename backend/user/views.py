from django.contrib.admin import action
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from user.models import UserBio

from user.serializers import UserBioSerializer

from user.mixins import IsOwnerMixin


class UserBioViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                        GenericViewSet):
    queryset = UserBio.objects.all()
    serializer_class = UserBioSerializer
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_permissions(self):
        if self.action == 'update':
             return [IsOwnerMixin()]
        else:
            return [AllowAny()]


