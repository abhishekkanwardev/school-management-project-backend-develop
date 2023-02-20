from rest_framework import permissions

from accounts.models import TeacherProfile


class IsAuthenticatedOrTeacherAdmin(permissions.IsAdminUser):
    
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False
        is_admin = super().has_permission(request, view) 
        is_teacher =  TeacherProfile.objects.filter(user = request.user).exists()
        return request.method in permissions.SAFE_METHODS or (is_admin or is_teacher) 

     
class IsAdminTeacherUser(permissions.BasePermission):
    """
    Allows access only to authenticated users and requestd user has admin role.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user = request.user.groups.all().values_list('name', flat=True)
        return bool('teacher' in user or 'admin' in user)

    
class IsStudentGuardianUser(permissions.BasePermission):
    """
    Allows access only to authenticated users and requestd user has admin role.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user = request.user.groups.all().values_list('name', flat=True)
        return bool('guardian' in user or '	student' in user)


class IsStudentUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user = request.user.groups.all().values_list('name', flat=True)
        return bool('student' in user)
    
    