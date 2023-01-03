

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'groups', 'user_permissions', 'password')


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
    
    def to_representation(self, instance):
        print("=================")
        r = super(MyTokenObtainPairSerializer, self).to_representation(instance)
        r.update({'user': self.user.username})
        return r
        