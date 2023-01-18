from django.contrib import admin
from .models import User, AdminProfile, PrincipalProfile, TeacherProfile

admin.site.register(User)
admin.site.register(AdminProfile)
admin.site.register(PrincipalProfile)
admin.site.register(TeacherProfile)