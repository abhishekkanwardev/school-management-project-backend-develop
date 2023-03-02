from rest_framework import serializers
from .models import GradingType, GradingKey, StudentGrades, LessonGrade, Grading

from school_process.serializers import LessonSerializer
from accounts.serializers import StudentDetailForContainsStudentsSerializer


class GradingTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GradingType
        fields = '__all__'
        read_only_fields = ['id']
        
    def validate_name(self, value):
        isNameExist = GradingType.objects.filter(name = value).exists()
        if isNameExist:
            raise serializers.ValidationError(f'{value} already exists in Grading Types.')
        return value


class GradingKeySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GradingKey
        fields = '__all__'
        read_only_fields = ['id']

    def validate_starting_mark(self, value):
        gradingKeys = GradingKey.objects.all()
        if gradingKeys:
            gradingKey = GradingKey.objects.order_by('-finish_mark').first()
            if gradingKey.finish_mark == 100:
                raise serializers.ValidationError(f'There is already defined grading keys for 0 to 100 grades. You should delete or update from has highest finish mark grading key!')
            elif (gradingKey.finish_mark + 1) != value:
                raise serializers.ValidationError(f'You should start your starting mark from {gradingKey.finish_mark + 1} for grading key. There is already defined grading key in that range!')
        else:
            if 0 != value:
                raise serializers.ValidationError(f'You should start your starting mark from 0 for grading key. There is no grading key defined before.')
        return value

    def validate(self, data):
        starting_mark = int(data['starting_mark'])
        finish_mark = int(data['finish_mark'])
        if starting_mark > finish_mark:
            raise serializers.ValidationError(f'The finish mark cannot be lower than the starting mark.')
        return data 

    def validate_rank_name(self, value):
        isRankNameExist = GradingKey.objects.filter(rank_name = value).exists()
        if isRankNameExist:
            raise serializers.ValidationError(f'{value} already exists in Grading Keys.')
        return value
        


class GradingSerializer(serializers.ModelSerializer):
    grading_type = GradingTypeSerializer(read_only=True) 
    
    class Meta:
        model = Grading
        fields = '__all__'
        read_only_fields = ['id']


class LessonGradeSerializer(serializers.ModelSerializer):
    grade_list = GradingSerializer(many=True, read_only=True) 
    lesson = LessonSerializer(read_only=True) 
    
    class Meta:
        model = LessonGrade
        read_only_fields = ['id']
        fields = '__all__'


class StudentGradesSerializer(serializers.ModelSerializer):
    lesson_grade_list = LessonGradeSerializer(many=True, read_only=True) 
    student = StudentDetailForContainsStudentsSerializer(read_only=True) 

    class Meta:
        model = StudentGrades
        fields = '__all__'
        read_only_fields = ['id']



