from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import GradingType, GradingKey, Grading, LessonGrade, StudentGrades
from .serializers import GradingTypeSerializer, GradingKeySerializer, GradingSerializer, LessonGradeSerializer, StudentGradesSerializer
from school_management.permission  import IsAuthenticatedOrTeacherAdmin
from rest_framework.pagination import LimitOffsetPagination



class GradingTypeListCreateAPIView(APIView, LimitOffsetPagination):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        grading_type_list = GradingType.objects.all()
        serializer = GradingTypeSerializer(grading_type_list, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = GradingTypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GradingTypeDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        grading_type_instance = get_object_or_404(GradingType, pk=pk)
        return grading_type_instance
        
    def get(self, request, pk):
        grading_type = self.get_object(pk = pk)
        serializer = GradingTypeSerializer(grading_type)
        return Response(serializer.data)

    def put(self, request, pk):
        grading_type = self.get_object(pk = pk)
        serializer = GradingTypeSerializer(grading_type, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        grading_type = self.get_object(pk = pk)
        grading_type.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


class GradingKeyListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        grading_key_list = GradingKey.objects.all()
        serializer = GradingKeySerializer(grading_key_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = GradingKeySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GradingKeyDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        grading_key_instance = get_object_or_404(GradingKey, pk=pk)
        return grading_key_instance
        
    def get(self, request, pk):
        grading_key = self.get_object(pk = pk)
        serializer = GradingKeySerializer(grading_key)
        return Response(serializer.data)

    def put(self, request, pk):
        grading_key = self.get_object(pk = pk)
        serializer = GradingKeySerializer(grading_key, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        grading_key = self.get_object(pk = pk)
        grading_key.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

class GradingListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        grading_list = Grading.objects.all()
        serializer = GradingSerializer(grading_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = GradingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GradingDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        grading_instance = get_object_or_404(Grading, pk=pk)
        return grading_instance
        
    def get(self, request, pk):
        grading = self.get_object(pk = pk)
        serializer = GradingSerializer(grading)
        return Response(serializer.data)

    def put(self, request, pk):
        grading = self.get_object(pk = pk)
        serializer = GradingSerializer(grading, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        grading = self.get_object(pk = pk)
        grading.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class LessonGradeListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        lesson_grade_list = LessonGrade.objects.all()
        serializer = LessonGradeSerializer(lesson_grade_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = LessonGradeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LessonGradeDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        lesson_grade_instance = get_object_or_404(LessonGrade, pk=pk)
        return lesson_grade_instance
        
    def get(self, request, pk):
        lesson_grade = self.get_object(pk = pk)
        serializer = LessonGradeSerializer(lesson_grade)
        return Response(serializer.data)

    def put(self, request, pk):
        lesson_grade = self.get_object(pk = pk)
        serializer = LessonGradeSerializer(lesson_grade, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        lesson_grade = self.get_object(pk = pk)
        lesson_grade.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class StudentGradesListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        student_grade_list = StudentGrades.objects.all()
        serializer = StudentGradesSerializer(student_grade_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = StudentGradesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StudentGradesDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        student_grade_instance = get_object_or_404(StudentGrades, pk=pk)
        return student_grade_instance
        
    def get(self, request, pk):
        student_grade = self.get_object(pk = pk)
        serializer = StudentGradesSerializer(student_grade)
        return Response(serializer.data)

    def put(self, request, pk):
        student_grade = self.get_object(pk = pk)
        serializer = StudentGradesSerializer(student_grade, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student_grade = self.get_object(pk = pk)
        student_grade.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class ClassGradesListCreateAPIView(APIView, LimitOffsetPagination):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request, pk):
        class_grade_list = StudentGrades.objects.filter(student__class_id=pk)
        results = self.paginate_queryset(class_grade_list, request, view=self)
        serializer = StudentGradesSerializer(results, many = True) 
        return self.get_paginated_response(serializer.data)
        
  
