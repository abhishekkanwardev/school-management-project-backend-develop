from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from accounts.models import StudentProfile
from school_management.utils import Response, ResponseMessage
from rest_framework import status
from .serializers import StudentSerializer, DismissalSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Dismissal, Class
from .permission import IsClassTeacherUser, IsTeacherUser, IsTeacherAdminUser
from rest_framework.generics import get_object_or_404
from school_management.permission  import IsAuthenticatedOrTeacherAdmin

from rest_framework.pagination import LimitOffsetPagination


class GetAllStudenForGuardian(APIView):
    
    def get_all_students(self, parent_id):
        return StudentProfile.objects.filter(guardian__user_id=parent_id)

    def get(self, request):
        students = self.get_all_students(request.user.id)
        serializer = StudentSerializer(students, many=True)
        return Response(data=serializer.data, code=status.HTTP_200_OK, message="All Students", status=True)        


class DismissalListByClassIdAPIView(APIView, LimitOffsetPagination):
    
    def get(self, request, classId):
        class_attendance_list = Dismissal.objects.filter(student__class_id=classId).order_by('pk')
        results = self.paginate_queryset(class_attendance_list, request, view=self)
        serializer = DismissalSerializer(results, many = True) 
        return self.get_paginated_response(serializer.data)


class DismissalViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Dismissal.objects.all()
    serializer_class = DismissalSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]
        elif self.request.method == 'GET':
            self.permission_classes = [IsTeacherAdminUser, ]
        else:
            self.permission_classes = [IsClassTeacherUser, ]
        return super(DismissalViewSet, self).get_permissions()
    
    def get_queryset(self):
        role = self.request.user.groups.values_list('name',flat = True)
        if 'admin' in role:
            obj = Dismissal.objects.all()
        elif 'teacher' in role:
            obj = Dismissal.objects.filter(student__class_id__class_teacher_id=3)
        else:
            obj = []
        return obj

    
class GetStudentByClassIdAPIView(APIView):

    def get(self, request, classId):
        _class = Class.objects.get(id = classId)
        studentsListByClass = _class.students.all()
        serializer = StudentSerializer(studentsListByClass,many = True) 
        return Response(data=serializer.data, code=status.HTTP_200_OK, message=ResponseMessage.SUCCESS, status=True)




# class DismissalViewSet(ModelViewSet):
#     permission_classes = [IsAdminUser]
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer
    

# class AdmissionViewSet(ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = AdmissionApplication.objects.all()
#     serializer_class = AdmissionApplicationSerializer
    
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             self.permission_classes = [AllowAny, ]
#         else:
#             self.permission_classes = [IsAdminUser, ]
#         return super(AdmissionViewSet, self).get_permissions()

