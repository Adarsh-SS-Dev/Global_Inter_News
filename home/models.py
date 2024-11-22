from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager



class Blog(models.Model):
    heading=models.CharField(max_length=5000, blank=True, null=True)
    img=models.ImageField(upload_to="pic", blank=True, null=True)
    desc=HTMLField()
    category=models.CharField(max_length=500, blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    slug=AutoSlugField(populate_from='heading',unique=True,null=True,default=None)
    hashtags=models.TextField(blank=True, null=True)
    tags=TaggableManager()


class Comment(models.Model):
    pro=models.ForeignKey(Blog,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    cmt=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)