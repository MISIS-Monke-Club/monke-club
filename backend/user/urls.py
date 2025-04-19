from django.urls import re_path
from .views import (
    BobritoBanditoDetail,
    CreateBobritoBandito,
)

urlpatterns = [
    re_path(r"^users/?$", CreateBobritoBandito.as_view(), name="user-create"),
    re_path(
        r"^users/(?P<username>[\w.@+-]+)/?$",
        BobritoBanditoDetail.as_view(),
        name="user-detail",
    ),
]
