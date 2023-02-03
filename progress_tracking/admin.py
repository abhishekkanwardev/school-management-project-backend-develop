from django.contrib import admin
from .models import ProggressRecord, LessonProgress, ProgressScore, StudentProgress, ClassProgress

admin.site.register(ClassProgress)
admin.site.register(ProggressRecord)
admin.site.register(LessonProgress)
admin.site.register(ProgressScore)
admin.site.register(StudentProgress)
