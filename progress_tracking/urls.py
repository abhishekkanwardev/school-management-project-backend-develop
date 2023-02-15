from django.urls import path,re_path

from .views import ProggressRecordListCreateAPIView, ProggressRecordDetailAPIView,StudentProgressListCreateAPIView, StudentProgressDetailAPIView, LessonProgressListCreateAPIView, LessonProgressDetailAPIView, ClassProgressListCreateAPIView 
    
urlpatterns = [
    path('class-progress/class/<int:classId>', ClassProgressListCreateAPIView.as_view(), name='class-progress-list'),
    re_path(r'^class-progress/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/class/(?P<classId>[0-9]+)/$',ClassProgressListCreateAPIView.as_view()),
    path('progress-record/list', ProggressRecordListCreateAPIView.as_view(), name='progress-record-list'),
    path('progress-record/detail/<int:pk>', ProggressRecordDetailAPIView.as_view(), name='progress-record-detail'),
    path('student-progress/list', StudentProgressListCreateAPIView.as_view(), name='student-progress-list'),
    path('student-progress/detail/<int:pk>', StudentProgressDetailAPIView.as_view(), name='student-progress-detail'),
    path('lesson-progress/list', LessonProgressListCreateAPIView.as_view(), name='lesson-progress-list'),
    path('lesson-progress/detail/<int:pk>', LessonProgressDetailAPIView.as_view(), name='lesson-progress-detail'),    
]