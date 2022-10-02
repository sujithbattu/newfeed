from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=500)
    keywords = models.TextField(max_length=4000)
    article_html = models.TextField()
    image_url = models.CharField(max_length=500)
    source = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publish_date = models.DateField(null=True)
    summary = models.TextField()
    dominant_color = models.CharField(max_length=100)
    contrast_color = models.CharField(max_length=100)
    article_url = models.CharField(max_length=1000)


class Comment(models.Model):
    message = models.CharField(max_length=500)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)


class Reply(models.Model):
    message = models.CharField(max_length=500)
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='replies', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
