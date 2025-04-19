from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    TunTunTunSahurRegisterSerializer,
    TunTunTunLogin,
    TunTunTunSahurSerializer,
)


class TunTunSaxurRegistrationView(generics.CreateAPIView):
    serializer_class = TunTunTunSahurRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = TunTunTunSahurRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "User successfully registered",
                "user": TunTunTunSahurSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class TunTunSaxurLoginView(TokenObtainPairView):
    serializer_class = TunTunTunLogin
