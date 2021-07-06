from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("auth.User", verbose_name=("author"), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    class Meta():
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
class Comment(models.Model):
    # related_name='comments' nos permite acceder desde el model Post
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
    class Meta():
        verbose_name = "Comment"
        verbose_name_plural = "Comments"