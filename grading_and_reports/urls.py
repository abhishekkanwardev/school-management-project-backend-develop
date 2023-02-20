from django.urls import path

from .views import GradingTypeDetailAPIView, GradingTypeListCreateAPIView, GradingKeyDetailAPIView, GradingKeyListCreateAPIView, GradingDetailAPIView, GradingListCreateAPIView, LessonGradeDetailAPIView, LessonGradeListCreateAPIView, StudentGradesDetailAPIView, StudentGradesListCreateAPIView, ClassGradesListCreateAPIView 
    
urlpatterns = [
  
    path('grading-type/list', GradingTypeListCreateAPIView.as_view(), name='grading-type-list'),
    path('grading-type/detail/<int:pk>', GradingTypeDetailAPIView.as_view(), name='grading-type-detail'),
    path('grading-key/list', GradingKeyListCreateAPIView.as_view(), name='grading-key-list'),
    path('grading-key/detail/<int:pk>', GradingKeyDetailAPIView.as_view(), name='grading-key-detail'),
    path('grading/list', GradingListCreateAPIView.as_view(), name='grading-list'),
    path('grading/detail/<int:pk>', GradingDetailAPIView.as_view(), name='grading-detail'),
    path('lesson-grade/list', LessonGradeListCreateAPIView.as_view(), name='lesson-grade-list'),
    path('lesson-grade/detail/<int:pk>', LessonGradeDetailAPIView.as_view(), name='lesson-grade-detail'),
    path('student-grade/list', StudentGradesListCreateAPIView.as_view(), name='student-grade-list'),
    path('student-grade/detail/<int:pk>', StudentGradesDetailAPIView.as_view(), name='student-grade-detail'),
    path('class-grade/detail/<int:pk>', ClassGradesListCreateAPIView.as_view(), name='class-grade-detail'),
   
]