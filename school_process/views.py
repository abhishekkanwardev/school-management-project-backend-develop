from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from accounts.models import StudentProfile
from school_management.utils import Response, ResponseMessage
from rest_framework import status
from .serializers import StudentSerializer, DismissalSerializer, ClassDismissalSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Dismissal, ClassDismissal
from .permission import IsClassTeacherUser, IsTeacherUser, IsTeacherAdminUser
from rest_framework.generics import get_object_or_404
from school_management.permission  import IsAuthenticatedOrTeacherAdmin



class GetAllStudenForGuardian(APIView):
    
    def get_all_students(self, parent_id):
        return StudentProfile.objects.filter(guardian__user_id=parent_id)

    def get(self, request):
        students = self.get_all_students(request.user.id)
        serializer = StudentSerializer(students, many=True)
        return Response(data=serializer.data, code=status.HTTP_200_OK, message="All Students", status=True)        


class ClassDismissalListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request, classId=None):
        class_dismissal_list = ClassDismissal.objects.order_by('pk')
        if classId:
            class_dismissal_list = class_dismissal_list.filter(pk = classId)
        serializer = ClassDismissalSerializer(class_dismissal_list, many = True) 
        return Response(serializer.data, code=status.HTTP_200_OK, message=ResponseMessage.SUCCESS, status=True)
        
    def post(self, request):
        serializer = ClassDismissalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ClassDismissalDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        class_dismissal_instance = get_object_or_404(ClassDismissal, pk=pk)
        return class_dismissal_instance
        
    def get(self, request, pk):
        class_dismissal = self.get_object(pk = pk)
        serializer = ClassDismissalSerializer(class_dismissal)
        return Response(serializer.data, code=status.HTTP_200_OK, message=ResponseMessage.SUCCESS, status=True)

    def put(self, request, pk):
        class_dismissal = self.get_object(pk = pk)
        serializer = ClassDismissalSerializer(class_dismissal, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        class_dismissal = self.get_object(pk = pk)
        class_dismissal.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


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

