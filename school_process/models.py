from django.db import models

# Create your models here.



class Class(models.Model):
    class_name = models.CharField(max_length=255)
    class_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.class_name
    


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255)
    lesson_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.lesson_name
    