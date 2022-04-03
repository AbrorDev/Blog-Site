from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    summary = RichTextField(blank=True,null=True)
    image = models.CharField(max_length=300)
    body = RichTextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    viewers = models.ManyToManyField(User,related_name='post_viewers',null=True,blank=True)

    class Meta:
        ordering = ['created_at']

    def total_views(self):
        return self.viewers.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.body