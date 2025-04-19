from rest_framework import viewsets,filters

from marketplace.mentors.models import Mentor

from marketplace.mentors.serializers import GetListMentorSerializer

from marketplace.mentors.serializers import GetDetailMentorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    lookup_field = 'user__username'
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ["count_successful_transactions"]
    ordering = ['-count_successful_transactions']
    ordering_labels = {
        "count_successful_transactions": "Успешных сделок (по возрастанию)",
        "-count_successful_transactions": "Успешных сделок (по убыванию)",
    }

    def get_serializer_class(self):
        if self.action == 'list':
            return GetListMentorSerializer

        elif self.action == 'retrieve':
            return GetDetailMentorSerializer
        else:
            return GetListMentorSerializer

    @action(detail=False, methods=["get"], url_path="ordering-fields")
    def get_ordering_fields(self, request):
        result = []
        for index, data in self.ordering_labels.items():
            result.append({"value": index, "label": data})

        return Response(result)




