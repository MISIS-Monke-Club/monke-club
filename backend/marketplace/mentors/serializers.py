from rest_framework import serializers

from marketplace.mentors.models import Mentor

from marketplace.models import Service

from marketplace.serializers import ServiceSerializer, SubjectSerializer


#rating
#photo






class GetListMentorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    full_name = serializers.SerializerMethodField()
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Mentor
        fields = ("username", "full_name", "services", "subjects", "count_successful_transactions")


    def get_full_name(self, obj):
        return (obj.user.first_name + " " + obj.user.last_name).strip()


class GetDetailMentorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    full_name = serializers.SerializerMethodField()
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Mentor
        fields = ("username", "full_name", "description", "services", "subjects", "count_successful_transactions")

    def get_full_name(self, obj):
        return (obj.user.first_name + " " + obj.user.last_name).strip()

