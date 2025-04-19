from user.models import UserBio

from marketplace.models import Subject, Service

class GeFiltersEndpoint:
    def __init__(self):
        self.courses = UserBio.objects.values_list("course", flat=True).distinct().order_by("course")
        self.subjects = Subject.objects.values("name").distinct()
        self.services = Service.objects.values("name").distinct()

    def get_filters(self):
        return {
            "courses": list(self.courses),
            "subjects": [{"value": s["name"], "label": s["name"].capitalize()} for s in self.subjects],
            "services": [{"value": s["name"], "label": s["name"].capitalize()} for s in self.services],
        }