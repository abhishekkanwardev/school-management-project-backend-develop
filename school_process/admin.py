from django.contrib import admin
from .models import Class, Dismissal, Lesson, ClassDismissal

admin.site.register(Class)
admin.site.register(Dismissal)
admin.site.register(Lesson)
admin.site.register(ClassDismissal)
