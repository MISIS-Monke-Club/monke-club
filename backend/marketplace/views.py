from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from marketplace.models import Service

from backend.marketplace.serializers import ServiceSerializer

