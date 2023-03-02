from rest_framework import serializers
from .models import ProggressRecord, ProgressScore, LessonProgress, StudentProgress
from accounts.serializers import StudentDetailForContainsStudentsSerializer
from school_process.serializers import LessonSerializer
    
class ProgressScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgressScore
        exclude = ['id']
        read_only_fields = ['id']
    
    def validate(self, data):
        progress_type = data['progress_type']
        score = data['score']
        anySameData = ProgressScore.objects.filter(progress_type = progress_type, score = score).exists()
        if anySameData:
            raise serializers.ValidationError(f'Progress Score already exist with {progress_type} - {score} values.')
        return data 


class LessonProgressSerializer(serializers.ModelSerializer):
    progressScore = ProgressScoreSerializer(many=True, read_only=True) 
    lesson = LessonSerializer(read_only=True) 

    
    class Meta:
        model = LessonProgress
        read_only_fields = ['id']
        exclude = ['student_progress']


class StudentProgressSerializer(serializers.ModelSerializer):
    lesson_progress_list = LessonProgressSerializer(many=True, read_only=True) 
    student = StudentDetailForContainsStudentsSerializer(read_only=True) 

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

