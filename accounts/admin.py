from django.contrib import admin
from .models import User, AdminProfile, PrincipalProfile, TeacherProfile, StudentProfile, GuardianProfile

admin.site.register(User)
admin.site.register(AdminProfile)
admin.site.register(PrincipalProfile)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(GuardianProfile)