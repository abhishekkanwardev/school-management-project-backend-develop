from django.contrib import admin
from .models import User, AdminProfile, PrincipalProfile

admin.site.register(User)
admin.site.register(AdminProfile)
admin.site.register(PrincipalProfile)