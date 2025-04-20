from vacancies.models import WorkType, Stack

class GeVacancyFiltersEndpoint:
    def get_filters(self):
        work_types = WorkType.objects.all().values("id", "title")
        stacks = Stack.objects.all().values("title")
        
        experience_options = [
            {"value": 0, "label": "Без опыта"},
            {"value": 1, "label": "1 год"},
            {"value": 2, "label": "2 года"},
            {"value": 3, "label": "3 года"},
            {"value": 5, "label": "5 лет +"},
        ]
        result = {
            "work_type": list(work_types),
            "stack": list(stacks),
            "experience": experience_options,
            "additional": [
                {"name": "has_price", "label": "Только с зарплатой"},
            ]
        }
        return result