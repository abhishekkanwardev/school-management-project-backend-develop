from rest_framework.permissions import BasePermission
from .models import Dismissal

class IsClassTeacherUser(BasePermission):
    """
    Allows access only to authenticated users and requestd user has admin role.
    """

    def has_permission(self, request, view):
        user = request.user.groups.all().values_list('name', flat=True)
        
        pk = view.kwargs.get('pk', None)
        if request.method == 'PUT' or request.method == 'PATCH':
            try:
                dismissal_obj = Dismissal.objects.get(pk=pk)
                if dismissal_obj.student.class_id.class_teacher.user.id == request.user.id:
                    return bool('teacher' in user and request.user.is_authenticated)
                else:
                    return False
            except Dismissal.DoesNotExist:
                return bool('teacher' in user and request.user.is_authenticated)
        else:
            return bool('teacher' in user and request.user.is_authenticated)

class IsTeacherUser(BasePermission):
    """
    Allows access only to authenticated users and requestd user has admin role.
    """

    def has_permission(self, request, view):
        user = request.user.groups.all().values_list('name', flat=True)
        return bool('teacher' in user and request.user.is_authenticated)
    

class IsTeacherAdminUser(BasePermission):
    """
    Allows access only to authenticated users and requestd user has admin role.
    """

    def has_permission(self, request, view):
        return True
        user = request.user.groups.all().values_list('name', flat=True)
        return bool(('teacher' in user or 'admin' in user) and request.user.is_authenticated)