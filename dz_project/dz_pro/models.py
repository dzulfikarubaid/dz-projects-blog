from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime, date
# Create your models here.
class Post(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = RichTextUploadingField(blank=True, null=True) 
    category = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.first_name) + ' ' + str(self.last_name)

    def get_absolute_url(self):
        return reverse('window')