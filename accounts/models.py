from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .utils import generate_employee_id, generate_otp
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail
from school_management.utils import ResponseMessage

class RolesChoices(models.TextChoices):
    ADMIN = 'admin'
    PRINCIPAL = 'principal'
    TEACHER = 'teacher'
    GUARDIAN = 'guardian'
    STUDENT = 'student'
    GATEKEEPER = 'gatekeeper'
    DRIVER = 'driver'
    
    


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(email, password, **extra_fields)

        return user



class User(AbstractUser):
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25)
    gender = models.CharField(max_length=25, choices=GENDER, default='Male')
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=55, null=True, blank=True)
    username = None
    
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    
    def __str__(self) -> str:
        return f"{self.email}"
    
    def add_to_group(self, group_name):
        try:
            group = Group.objects.get(name=group_name)
        except Exception as e:
            group = Group.objects.create(name=group_name)
        self.groups.add(group)
        
    def send_forget_password_email(self):
        try:
            otp_obj = Otp.objects.create(user_id=self.id, otp=generate_otp(), type='ForgotPassword')
            message = f"This is your forgot passord code {otp_obj.otp}"
            send_mail(ResponseMessage.FORGET_PASSWORD_SUBJECT, message, settings.EMAIL_HOST_USER, [self.email])
            return True
        except Exception as e:
            return False
        
    def send_reset_password_mail(self):
        try:
            otp_obj = Otp.objects.create(user_id=self.id, otp=generate_otp(), type='ResetPassword')
            message = f"This is your reset passord code {otp_obj.otp}"
            send_mail(ResponseMessage.RESET_PASSWORD_SUBJECT, message, settings.EMAIL_HOST_USER, [self.email])
            return True
        except Exception as e:
            return False
    
    
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=55)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.email}"
    
    def save(self, *args, **kwargs):
        self.employee_id = generate_employee_id()
        super(AdminProfile, self).save(*args, **kwargs)
    

class PrincipalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=55)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    appointed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.email}"
    
    def save(self, *args, **kwargs):
        self.employee_id = generate_employee_id()
        super(PrincipalProfile, self).save(*args, **kwargs)
    
    
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=55)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    qualification = models.CharField(max_length=255)
    year_of_experience = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.employee_id = generate_employee_id()
        super(TeacherProfile, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.user.email
        

class GuardianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    relation = models.CharField(max_length=55, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.email
    
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.CharField(max_length=255)
    class_id = models.ForeignKey('school_process.Class', on_delete=models.CASCADE, null=True, blank=True)
    guardian = models.OneToOneField(GuardianProfile, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.email
    

    
class Otp(models.Model):
    TYPE = (
        ('CreateAccount','CreateAccount'),
        ('ForgotPassword','ForgotPassword'),
        ('ResetPassword','ResetPassword'),
    )
    
    otp = models.CharField(max_length=55)
    type = models.CharField(max_length=55, choices=TYPE, default='CreateAccount')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user.email}-{self.type}"
    