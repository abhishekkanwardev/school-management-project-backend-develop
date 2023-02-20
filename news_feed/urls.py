from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers
from .views import FeedViewSet, FeedCommentViewSet, FeedPostLikeViewSet



feed_api_router = routers.SimpleRouter()
feed_api_router.register("post", FeedViewSet)
feed_api_router.register("post-like", FeedPostLikeViewSet)
feed_api_router.register("comment", FeedCommentViewSet)

urlpatterns = [
    path("", include(feed_api_router.urls), name='feed_api'),
]
