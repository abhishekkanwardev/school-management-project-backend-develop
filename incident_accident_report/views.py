from django.shortcuts import render
from .models import IncidentAccidentReport
from .serializers import IncidentAccidentReportSErializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from school_management.permission import IsAdminTeacherUser, IsStudentGuardianUser
from school_management.utils import CustomPagination
from rest_framework.pagination import LimitOffsetPagination



class IncidentAccidentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IncidentAccidentReport.objects.all()
    serializer_class = IncidentAccidentReportSErializer
    pagination_class = LimitOffsetPagination
    
    
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsStudentGuardianUser, ]
        else:
            self.permission_classes = [IsAdminTeacherUser, ]
        return super(IncidentAccidentViewSet, self).get_permissions()
    
    def get_queryset(self):  
        role = self.request.user.groups.values_list('name',flat = True)
        if 'admin' in role or 'teacher' in role:
            self.queryset = IncidentAccidentReport.objects.all()
        elif 'student' in role:
            self.queryset = IncidentAccidentReport.objects.filter(student__user__user_id=self.request.user.id)
        elif 'guardian' in role:
            self.queryset = IncidentAccidentReport.objects.filter(student__guardian__user_id=self.request.user.id)
        return super(IncidentAccidentViewSet, self).get_queryset()