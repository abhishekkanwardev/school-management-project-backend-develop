from rest_framework import serializers
from .models import Class,Lesson
    

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = ['id']


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        read_only_fields = ['id', 'created_at', 'updated_at']
        exclude = ['created_at','updated_at']




