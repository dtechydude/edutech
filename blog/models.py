from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_img = models.ImageField(default='post_pic1.jpg', upload_to='post_pics')
    #content = RichTextField(blank=True, null=True)
    content = CKEditor5Field('Text', config_name='extends')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='like_post')

    def total_likes(self):
        return self.likes.count()


    def __self__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    
class Comment (models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)