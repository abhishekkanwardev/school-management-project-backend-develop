from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import ProggressRecord, StudentProgress, LessonProgress
from .serializers import ProggressRecordSerializer, StudentProgressSerializer, LessonProgressSerializer
from school_management.permission  import IsAuthenticatedOrTeacherAdmin
from rest_framework.pagination import LimitOffsetPagination



class ClassProgressListCreateAPIView(APIView, LimitOffsetPagination):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request, classId, year=None, month=None, day=None):
        class_progress_list = ProggressRecord.objects.all()
        studentProgressList = StudentProgress.objects.filter(student__class_id = classId)        

        if year and month and day:
            class_progress_filtered = class_progress_list.filter(date__year = year, date__month = month, date__day = day)
            if class_progress_filtered:
                class_progress = class_progress_filtered.first()
                filteredStudentProgress = studentProgressList.filter(progress_record__pk = class_progress.pk)
                results = self.paginate_queryset(filteredStudentProgress, request, view=self)
                serializer = StudentProgressSerializer(results, many = True) 

                return self.get_paginated_response(serializer.data)

            return Response()
        

        dataAsscociated = list()
        for i in class_progress_list:
            filteredStudentProgress = studentProgressList.filter(progress_record__pk = i.pk)
            serializer = StudentProgressSerializer(filteredStudentProgress, many = True) 
            dataAsscociated.append({'date':i.date, 'student_progress_list': serializer.data})

        return Response(dataAsscociated)



class ProggressRecordListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        progress_record_list = ProggressRecord.objects.all()
        serializer = ProggressRecordSerializer(progress_record_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ProggressRecordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProggressRecordDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        progress_record_instance = get_object_or_404(ProggressRecord, pk=pk)
        return progress_record_instance
        
    def get(self, request, pk):
        progress_record = self.get_object(pk = pk)
        serializer = ProggressRecordSerializer(progress_record)
        return Response(serializer.data)

    def put(self, request, pk):
        progress_record = self.get_object(pk = pk)
        serializer = ProggressRecordSerializer(progress_record, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        progress_record = self.get_object(pk = pk)
        progress_record.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

class StudentProgressListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        student_progress_list = StudentProgress.objects.all()
        serializer = StudentProgressSerializer(student_progress_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = StudentProgressSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StudentProgressDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        student_progress_instance = get_object_or_404(StudentProgress, pk=pk)
        return student_progress_instance
        
    def get(self, request, pk):
        student_progress = self.get_object(pk = pk)
        serializer = StudentProgressSerializer(student_progress)
        return Response(serializer.data)

    def put(self, request, pk):
        student_progress = self.get_object(pk = pk)
        serializer = StudentProgressSerializer(student_progress, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student_progress = self.get_object(pk = pk)
        student_progress.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



class LessonProgressListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request):
        lesson_progress_list = LessonProgress.objects.all()
        serializer = LessonProgressSerializer(lesson_progress_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = LessonProgressSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LessonProgressDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        lesson_progress_instance = get_object_or_404(LessonProgress, pk=pk)
        return lesson_progress_instance
        
    def get(self, request, pk):
        lesson_progress = self.get_object(pk = pk)
        serializer = LessonProgressSerializer(lesson_progress)
        return Response(serializer.data)

    def put(self, request, pk):
        lesson_progress = self.get_object(pk = pk)
        serializer = LessonProgressSerializer(lesson_progress, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        lesson_progress = self.get_object(pk = pk)
        lesson_progress.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    