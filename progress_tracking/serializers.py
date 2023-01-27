from rest_framework import serializers
from .models import ProggressRecord, ProgressScore, LessonProgress, StudentProgress

from school_process.serializers import LessonSerializer
    
class ProgressScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgressScore
        fields = '__all__'
        read_only_fields = ['id']


class LessonProgressSerializer(serializers.ModelSerializer):
    progressScore = ProgressScoreSerializer(many=True, read_only=True) 
    lesson = LessonSerializer(read_only=True) 

    
    class Meta:
        model = LessonProgress
        read_only_fields = ['id']
        exclude = ['student_progress']


class StudentProgressSerializer(serializers.ModelSerializer):
    
    lesson_progress_list = LessonProgressSerializer(many=True, read_only=True) 

    class Meta:
        model = StudentProgress
        fields = '__all__'
        read_only_fields = ['id']

class ProggressRecordSerializer(serializers.ModelSerializer):
    
    student_progress_list = StudentProgressSerializer(many=True, read_only=True) 

    class Meta:
        model = ProggressRecord
        fields = '__all__'
        read_only_fields = ['id']
