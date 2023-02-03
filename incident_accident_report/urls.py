from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers
from .views import IncidentAccidentViewSet



incident_accident_api_router = routers.SimpleRouter()
incident_accident_api_router.register("", IncidentAccidentViewSet)

urlpatterns = [
    path("", include(incident_accident_api_router.urls), name='incident_accident_api'),
]
