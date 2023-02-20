from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers
from .views import ClassViewSet, AdmissionViewSet, AppointmentViewSet, AppointmentTimeAvailableStateList, AppointmentUpdateStatusById

app_name = 'admission_process'

class_api_router = routers.SimpleRouter()
class_api_router.register("class", ClassViewSet)

admission_api_router = routers.SimpleRouter()
admission_api_router.register("admission", AdmissionViewSet)
admission_api_router.register("appointment", AppointmentViewSet)

urlpatterns = [
    path("", include(class_api_router.urls), name='class_api'),
    path("", include(admission_api_router.urls), name='admission_api'),
    path('time-available-state/list', AppointmentTimeAvailableStateList.as_view(), name='time-available-state-list'),
    path('update-appointment/<int:pk>', AppointmentUpdateStatusById.as_view(), name='update-appointment'),

]
