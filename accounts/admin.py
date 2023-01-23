from django.contrib import admin
from .models import User, AdminProfile, PrincipalProfile, TeacherProfile, GuardianProfile, StudentProfile

admin.site.register(User)
admin.site.register(AdminProfile)
admin.site.register(PrincipalProfile)
admin.site.register(TeacherProfile)
admin.site.register(GuardianProfile)
admin.site.register(StudentProfile)