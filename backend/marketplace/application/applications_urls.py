from django.urls import path
from .application_views import (
    ApplicationListCreateView as Alcv,
    ApplicationRUDView as Arud,
    ApplicationFilterFieldsView,
    ApplicationOrderingFieldsView
)


urlpatterns = [
    path("filter-fields/", ApplicationFilterFieldsView.as_view(), name="application-filter-fields"),
    path("ordering-fields/", ApplicationOrderingFieldsView.as_view(), name="application-ordering-fields"),
    path("", Alcv.as_view(), name="application-list-create"),
    path("<slug:slug>/", Arud.as_view(), name="application-detail"),
]
