from rest_framework import serializers
from .models import Post, PostImage, Comment, Like


class PostImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = PostImage
        fields = ['id', 'url']
        
    def get_url(self, instance):
        request = self.context.get('request')
        return str(request.build_absolute_uri(instance.image.url))


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'images']
        
    def get_images(self, instance):
        request = self.context.get('request')
        images = PostImage.objects.filter(post_id=instance.id)
        serializer = PostImageSerializer(images, many=True, context={"request": request})
        return serializer.data
        
    def create(self, validated_data):
        request = self.context['request']
        images_data = request.FILES.getlist('image')

        validated_data.update({'user':request.user})
        
        post = Post.objects.create(**validated_data)
        
        for image in images_data:
            PostImage.objects.create(post=post, image=image)
        return post
    

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"
        

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        