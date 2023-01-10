from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers
from .views import ClassViewSet, AdmissionViewSet

class_api_router = routers.SimpleRouter()
class_api_router.register("class", ClassViewSet)
admission_api_router = routers.SimpleRouter()
admission_api_router.register("", AdmissionViewSet)

urlpatterns = [
    path("", include(class_api_router.urls)),
    path("", include(admission_api_router.urls)),
    # Automatically Created API URLs from the Router:
    # /games/api/     - list of all games (url name is 'game-list')
    # /games/api/<pk> - detail of a single game based on its pk
    #                   (url name is 'game-detail')
]
