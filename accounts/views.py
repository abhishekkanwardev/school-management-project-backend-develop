from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import MyTokenObtainPairSerializer


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
