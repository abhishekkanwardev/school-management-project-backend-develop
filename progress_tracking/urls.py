from django.urls import path,re_path

from .views import ProggressRecordListCreateAPIView, ProggressRecordDetailAPIView,StudentProgressListCreateAPIView, StudentProgressDetailAPIView, LessonProgressListCreateAPIView, LessonProgressDetailAPIView, ClassProgressDetailAPIView, ClassProgressListCreateAPIView 
    
urlpatterns = [
    path('class-progress/list', ClassProgressListCreateAPIView.as_view(), name='class-progress-list'),
    path('class-progress/class/<int:classId>', ClassProgressListCreateAPIView.as_view(), name='class-progress-list'),
    path('class-progress/detail/<int:pk>', ClassProgressDetailAPIView.as_view(), name='class-progress-detail'),    
    path('progress-record/list', ProggressRecordListCreateAPIView.as_view(), name='progress-record-list'),
    path('progress-record/detail/<int:pk>', ProggressRecordDetailAPIView.as_view(), name='progress-record-detail'),
    path('student-progress/list', StudentProgressListCreateAPIView.as_view(), name='student-progress-list'),
    path('student-progress/detail/<int:pk>', StudentProgressDetailAPIView.as_view(), name='student-progress-detail'),
    path('lesson-progress/list', LessonProgressListCreateAPIView.as_view(), name='lesson-progress-list'),
    path('lesson-progress/detail/<int:pk>', LessonProgressDetailAPIView.as_view(), name='lesson-progress-detail'),    
]