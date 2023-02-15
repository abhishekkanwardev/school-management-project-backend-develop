from django.contrib import admin
from .models import ProggressRecord, LessonProgress, ProgressScore, StudentProgress

admin.site.register(ProggressRecord)
admin.site.register(LessonProgress)
admin.site.register(ProgressScore)
admin.site.register(StudentProgress)
