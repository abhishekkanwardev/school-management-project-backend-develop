from rest_framework import serializers
from accounts.models import StudentProfile
from .models import Class, Dismissal



class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class_id = serializers.SerializerMethodField()
    
    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'profile_image', 'bio', 'class_id', 'guardian',]
        
    def get_class_id(self, instance):
        serializer = ClassSerializer(instance.class_id)
        return serializer.data
    
    
class DismissalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dismissal
        fields = "__all__"