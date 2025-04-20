from vacancies.models import WorkType, Stack


class GeVacancyFiltersEndpoint:
    def get_filters(self):
        work_types = WorkType.objects.all().values("id", "title")
        stacks = Stack.objects.all().values("id", "title")

        result = {
            "work_type": list(work_types),
            "stack": list(stacks),
        }
        return result