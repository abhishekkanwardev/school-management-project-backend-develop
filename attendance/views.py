from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from school_management.permission  import IsAuthenticatedOrTeacherAdmin
from .models import Attendance, ClassAttendance
from .serializers import AttendanceSerializer, ClassAttendanceSerializer



class ClassAttendanceListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request, classId=None):
        class_attendance_list = ClassAttendance.objects.order_by('pk')
        if classId:
            class_attendance_list = class_attendance_list.filter(pk = classId)
        serializer = ClassAttendanceSerializer(class_attendance_list, many = True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ClassAttendanceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ClassAttendanceDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get_object(self,pk):
        class_attendance_instance = get_object_or_404(ClassAttendance, pk=pk)
        return class_attendance_instance
        
    def get(self, request, pk):
        class_attendance = self.get_object(pk = pk)
        serializer = ClassAttendanceSerializer(class_attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        class_attendance = self.get_object(pk = pk)
        serializer = ClassAttendanceSerializer(class_attendance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        class_attendance = self.get_object(pk = pk)
        class_attendance.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    



class AttendanceListCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticatedOrTeacherAdmin]

    def get(self, request, student_id=None, year=None, month=None, day=None):
        attendance_list = Attendance.objects.order_by('lesson_period')
        if student_id:
            attendance_list = attendance_list.filter(student__id = student_id)
            if year and month and day:
                attendance_list = attendance_list.filter(date__year = year, date__month = month, date__day = day)
        serializer = AttendanceSerializer(attendance_list,many = True) 
        return Response(serializer.data)
        
    def post(self, request, student_id=None, year=None, month=None, day=None):
        serializer = AttendanceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AttendanceDetailAPIView(APIView):

    permission_classes = [IsAuthenticatedOrTeacherAdmin]
    
    def get_object(self,pk):
        attendance_intance = get_object_or_404(Attendance, pk=pk)
        return attendance_intance
        
    def get(self, request, pk):
        attendance = self.get_object(pk = pk)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        attendance = self.get_object(pk = pk)
        serializer = AttendanceSerializer(attendance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        attendance = self.get_object(pk = pk)
        attendance.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

