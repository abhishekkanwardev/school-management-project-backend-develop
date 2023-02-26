from django.urls import include, path, re_path
from django.views.generic import RedirectView
from rest_framework import routers
from .views import ClassViewSet, AdmissionViewSet, AppointmentViewSet, AppointmentTimeAvailableStateList, AppointmentUpdateStatusById, AdmissionApplicationNonAuthDetailAPIView

app_name = 'admission_process'

class_api_router = routers.SimpleRouter()
class_api_router.register("class", ClassViewSet)

admission_api_router = routers.SimpleRouter()
admission_api_router.register("admission", AdmissionViewSet)
admission_api_router.register("appointment", AppointmentViewSet)

urlpatterns = [
    path("", include(class_api_router.urls), name='class_api'),
    path("", include(admission_api_router.urls), name='admission_api'),
    path('update-appointment/<int:pk>', AppointmentUpdateStatusById.as_view(), name='update-appointment'),
    re_path(r'^time-available-state/date/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$',AppointmentTimeAvailableStateList.as_view()),
    path('appointment-non-auth/detail/<int:pk>', AdmissionApplicationNonAuthDetailAPIView.as_view(), name='appointment-non-auth'),

]
