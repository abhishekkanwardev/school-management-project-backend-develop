from django.db import models
from accounts.models import StudentProfile, TeacherProfile



class Class(models.Model):
    class_name = models.CharField(max_length=255)
    class_description = models.CharField(max_length=255)
    class_teacher = models.ForeignKey(TeacherProfile, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.class_name

class Dismissal(models.Model):
    DISMISSAL_TYPE = (
        ('Regular', 'Regular'),
        ('Early', 'Early')
    )
    STATUS = (
        ('Waiting', 'Waiting'),
        ('Approved', 'Approved'),
        ('Reject', 'Reject'),
    )
    student = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING)
    dismissal_type = models.CharField(choices=DISMISSAL_TYPE, default='Regular', max_length=10)
    notes = models.TextField()
    document = models.FileField(upload_to='images/', null=True, blank=True)
    status = models.CharField(choices=STATUS, default="Waiting", max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.student.user.email
    


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255)
    lesson_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.lesson_name
    

