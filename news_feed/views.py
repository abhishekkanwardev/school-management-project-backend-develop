from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, PostLikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from school_management.permission import IsAdminTeacherUser, IsStudentGuardianUser
from school_management.utils import CustomPagination


class FeedViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    
    def get_serializer_context(self):
        return {"request": self.request}    
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminTeacherUser, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(FeedViewSet, self).get_permissions()
    
    
class FeedPostLikeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer
    pagination_class = CustomPagination
    
    def get_serializer_context(self):
        return {"request": self.request}
    
    
class FeedCommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    
    def get_serializer_context(self):
        return {"request": self.request}    
    
   
    