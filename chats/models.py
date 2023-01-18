from django.db import models
from accounts.models import User


# class Chat(models.Model):
#     user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
#     user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f"{self.user1}-{self.user2}"


# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
#     chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
#     content = models.CharField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.content
    
    

class Chat(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_group = models.BooleanField()
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)