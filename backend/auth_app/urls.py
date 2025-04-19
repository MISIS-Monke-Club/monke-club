from django.urls import re_path
from auth_app.views import (
    TunTunSaxurRegistrationView,
    TunTunSaxurLoginView,
)

urlpatterns = [
    re_path(r"^login/?$", TunTunSaxurLoginView.as_view(), name="user_login"),
    re_path(
        r"^register/?$", TunTunSaxurRegistrationView.as_view(), name="user_register"
    ),
]
