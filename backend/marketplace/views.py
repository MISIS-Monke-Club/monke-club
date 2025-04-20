from .models import Subject, Service
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServiceSerializer, SubjectSerializer


class BombiniGusiniSubject(APIView):
    def get(self, request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BombiniGusiniService(APIView):
    def get(self, request):
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

