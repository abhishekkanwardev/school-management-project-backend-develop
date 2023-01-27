from rest_framework import permissions

from accounts.models import TeacherProfile


class IsAuthenticatedOrTeacherAdmin(permissions.IsAdminUser):
    
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False
        is_admin = super().has_permission(request, view) 
        is_teacher =  TeacherProfile.objects.filter(user = request.user).exists()
        return request.method in permissions.SAFE_METHODS or (is_admin or is_teacher) 

     