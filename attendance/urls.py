from django.urls import path,re_path

from .views import AttendanceListCreateAPIView,AttendanceDetailAPIView

urlpatterns = [
    path('attendance-list', AttendanceListCreateAPIView.as_view(), name='attendance-list'),
    path('detail/<int:pk>', AttendanceDetailAPIView.as_view(), name='attendance-detail'),
    path('student-<int:student_id>', AttendanceListCreateAPIView.as_view(), name='student-attendances'),
    re_path(r'^student-(?P<student_id>[0-9]+)/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$',AttendanceListCreateAPIView.as_view()),
]