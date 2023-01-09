from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import MyTokenObtainPairSerializer, UserSerializer, UserRegisterSerializer, ForgatePasswordSerializer, SavePasswordSerializer, SaveResetPasswordSerializer, AdminSerializer, AdminRegistrationSerializer
from rest_framework.response import Response as DefaultResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from school_management.utils import Response, ResponseMessage
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Otp
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema

User = get_user_model()


class UserRegistration(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=UserRegisterSerializer,
        operation_id='User Registration API',
        security=[],
        operation_description='This endpoint used for user Registration'
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data, context={'request': request.data})
        
        if serializer.is_valid():
            try:
                data = serializer.save()
                return Response(data=data, code=status.HTTP_200_OK, message=ResponseMessage.SUCCESS, status=True)
            except Exception as e:
                return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=DefaultResponse(e.detail.__dict__), status=False)
        else:
            return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=serializer.errors, status=False)
        


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=MyTokenObtainPairSerializer,
        operation_id='Login API',
        security=[],
        operation_description='This endpoint used for user login'
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid()
        except Exception as e:
            return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=str(e), status=False)
        
        return Response(data=serializer.validated_data, code=status.HTTP_200_OK, message=ResponseMessage.SUCCESS, status=True)
    

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_id='Login API',
        security=[],
        operation_description='This endpoint used for user login'
    )
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(code=status.HTTP_205_RESET_CONTENT, data={}, status=True, message=ResponseMessage.LOGOUT)
        except Exception as e:
            return Response(code=status.HTTP_400_BAD_REQUEST, data={}, status=False, message=str(e))
        
        
class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_id='Login API',
        security=[],
        operation_description='This endpoint used for user login'
    )
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(code=status.HTTP_205_RESET_CONTENT, data={}, status=True, message=ResponseMessage.LOGOUT)
    
    
    
class ForgatePasswordView(APIView):
    """
    This class used for forgate user password
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=ForgatePasswordSerializer,
        operation_id='Login API',
        security=[],
        operation_description='This endpoint used for user login'
    )
    def post(self, request):
        """
        This method responsible for handle POST request
        """
        serializer = ForgatePasswordSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.data['email'])
            except User.DoesNotExist:
                return Response(code=status.HTTP_404_NOT_FOUND, data={}, status=False, message=ResponseMessage.USER_NOT_FOUND_BY_EMAIL)
            mail = user.send_forget_password_email()
            if mail:
                return Response(code=status.HTTP_200_OK, data={}, status=True, message=ResponseMessage.FORGOT_PASSWORD_MAIL_SEND_SUCCESS)
            else:
                return Response(code=status.HTTP_400_BAD_REQUEST, data={}, status=True, message=ResponseMessage.SOMETHING_WENT_WRONG)
            
            
class ResetPassword(APIView):
    
    @swagger_auto_schema(
        tags=["Authentication"],
        operation_id='Login API',
        security=[],
        operation_description='This endpoint used for user login'
    )
    def post(self, request):
        """
        This method responsible for handle POST request
        """
        user = request.user
        try:
            mail = user.send_reset_password_mail()
            if mail:
                return Response(code=status.HTTP_200_OK, data={}, status=True, message=ResponseMessage.RESET_PASSWORD_MAIL_SEND_SUCCESS)
            else:
                return Response(code=status.HTTP_400_BAD_REQUEST, data={}, status=True, message=ResponseMessage.SOMETHING_WENT_WRONG)
        except Exception as e:
            return Response(code=status.HTTP_400_BAD_REQUEST, data={}, status=True, message=ResponseMessage.SOMETHING_WENT_WRONG)


class SaveResetPassword(APIView):
    
    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=SaveResetPasswordSerializer,
        operation_id='Login API',
        security=[],
        operation_description='This endpoint used for user login'
    )
    def post(self, request):
        user = request.user
        serializer = SaveResetPasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                otp_obj = Otp.objects.get(user__email=user.email, otp=serializer.data['otp'], type='ResetPassword')
                if otp_obj:
                    if otp_obj.otp == serializer.data['otp']:
                        user.password = make_password(serializer.data['password'])
                        user.save()
                        otp_obj.delete()
                        return Response(code=status.HTTP_200_OK, data={}, status=True, message=ResponseMessage.PASSWORD_CHANGED)
            except Otp.DoesNotExist:
                return Response(code=status.HTTP_400_BAD_REQUEST, data={}, status=False, message=ResponseMessage.Invalid_OTP)
        else:
            return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=serializer.errors, status=False)
        


class SavePasswordView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=SavePasswordSerializer,
        operation_id='Save Password',
        security=[],
        operation_description='This endpoint used for save new password'
    )
    def post(self, request):
        """
        This method responsible for handle POST request
        """
        
        serializer = SavePasswordSerializer(data=request.data)

        if serializer.is_valid():
            try:
                otp_obj = Otp.objects.get(user__email=serializer.data['email'], otp=serializer.data['otp'])
                if otp_obj:
                    if otp_obj.otp == serializer.data['otp']:
                        user = User.objects.filter(email=otp_obj.user.email).first()
                        user.password = make_password(serializer.data['password'])
                        user.save()
                        otp_obj.delete()
                        return Response(code=status.HTTP_200_OK, data={}, status=True, message=ResponseMessage.PASSWORD_CHANGED)

            except Otp.DoesNotExist:
                return Response(code=status.HTTP_400_BAD_REQUEST, data={}, status=False, message=ResponseMessage.Invalid_OTP)
        else:
            return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=serializer.errors, status=False)
        
        
class AdminRegisterView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = AdminRegistrationSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            try:
                data = serializer.save()
                return Response(data=data, code=status.HTTP_200_OK, message=ResponseMessage.SUCCESS, status=True)
            except Exception as e:
                return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=DefaultResponse(e.detail.__dict__), status=False)
        else:
            return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=serializer.errors, status=False)