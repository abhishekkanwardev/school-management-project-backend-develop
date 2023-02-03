from django.urls import path,re_path

from .views import AttendanceListCreateAPIView,AttendanceDetailAPIView, ClassAttendanceListCreateAPIView, ClassAttendanceDetailAPIView

urlpatterns = [
    path('class-attendance/list', ClassAttendanceListCreateAPIView.as_view(), name='class-attendance-list'),
    path('class-attendance/class/<int:classId>', ClassAttendanceListCreateAPIView.as_view(), name='class-attendance-list'),
    path('class-attendance/detail/<int:pk>', ClassAttendanceDetailAPIView.as_view(), name='class-attendance-detail'),   
    path('attendance-list', AttendanceListCreateAPIView.as_view(), name='attendance-list'),
    path('detail/<int:pk>', AttendanceDetailAPIView.as_view(), name='attendance-detail'),
    path('student/<int:student_id>', AttendanceListCreateAPIView.as_view(), name='student-attendances'),
    re_path(r'^student-(?P<student_id>[0-9]+)/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$',AttendanceListCreateAPIView.as_view()),
]