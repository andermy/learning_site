from rest_framework import serializers
from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description'
        )
        model = models.Course