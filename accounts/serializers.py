

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import serializers

from django.contrib.auth import get_user_model
from school_management.utils import Response
from rest_framework import status
from django.contrib.auth.models import Group
from .models import AdminProfile, PrincipalProfile
from django.forms.models import model_to_dict

User = get_user_model()



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        exclude = ("employee_id", "user")
        
    def to_representation(self, instance):
        data = super(AdminSerializer, self).to_representation(instance)
        data.update({"employee_id": instance.employee_id})
        return data
        
    def create(self, validated_data):
        return super().create(validated_data)
        

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalProfile
        exclude = ("employee_id", "user")
        
    def to_representation(self, instance):
        data = super(PrincipalSerializer, self).to_representation(instance)
        data.update({"employee_id": instance.employee_id})
        return data
        
    def create(self, validated_data):
        return super().create(validated_data)



class UserRegisterSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField()
    role = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'gender', 'address', 'country', 'user_type', 'password', 'role']
        extra_kwargs = {
            'user_type': {'write_only': True},
            'gender':{'required':False}
        }
        
    def validate(self, data):
        """
        Check version already existo or not for this corporate
        """
        if data['user_type'] == 'admin':
            seializer = AdminSerializer(data=data)
        elif data['user_type'] == 'principal':
            seializer = PrincipalSerializer(data=data)
            
        if seializer.is_valid():
            return data
        else:
            raise serializers.ValidationError(seializer.errors)
        
    def get_role(self, instance):
        return instance.groups.values_list('name', flat=True)
    
    def create(self, validated_data):
        request_data = self.context.get('request').data
        if validated_data['user_type'] == 'admin':
            seializer = AdminSerializer(data=request_data)
        elif validated_data['user_type'] == 'principal':
            seializer = PrincipalSerializer(data=request_data)
            
        if seializer.is_valid():
            obj = User.objects.create_user(email=validated_data['email'], phone_number=validated_data['phone_number'], address=validated_data['address'], country=validated_data.get('country'), password=validated_data['password'])
            seializer.save(user=obj)
            obj.add_to_group(validated_data['user_type'])

            d = {**model_to_dict(obj, fields=[field.name for field in obj._meta.fields]), **seializer.data}
            d['role'] = self.get_role(obj)
            
            return d
        else:
            raise serializers.ValidationError(seializer.errors)
        

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'groups', 'user_permissions', 'password')
        
    def get_role(self, instance):
        return instance.groups.values_list('name', flat=True)
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        user = UserSerializer(self.user)
        data['user'] = user.data

        return data


class ForgatePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
    
class SavePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
class SaveResetPasswordSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)
    password = serializers.CharField(required=True)