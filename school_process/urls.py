from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers
from .views import GetAllStudenForGuardian, DismissalViewSet, DismissalListByClassIdAPIView, GetStudentByClassIdAPIView

# app_name = 'admission_process'

dismissal_api_router = routers.SimpleRouter()
dismissal_api_router.register("dismissal", DismissalViewSet)


urlpatterns = [
    path("get-all-students-by-guardian", GetAllStudenForGuardian.as_view(), name='get_all_students_by_guardian'),
    path("", include(dismissal_api_router.urls), name='dismissal_api'),
    path('class-dismissal/class/<int:classId>', DismissalListByClassIdAPIView.as_view(), name='class-dismissal-list'),
    path('student-list/class/<int:classId>', GetStudentByClassIdAPIView.as_view(), name='student-list-by-class'),
]
