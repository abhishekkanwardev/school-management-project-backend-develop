from django.contrib import admin
from .models import GradingType, GradingKey, Grading, LessonGrade, StudentGrades


admin.site.register(GradingType)
admin.site.register(GradingKey)
admin.site.register(Grading)
admin.site.register(LessonGrade)
admin.site.register(StudentGrades)
