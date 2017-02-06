from rest_framework import generics

from . import models
from . import serializers

class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class RetrieveUpdateDestroyCourse(generics.RetrieveDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer