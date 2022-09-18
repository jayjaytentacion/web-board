from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=265)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE)
    starter = models.ForeignKey(get_user_model(), related_name='topics',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=5000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), related_name='posts',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(get_user_model(), null=True, related_name='+',on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.message
        

