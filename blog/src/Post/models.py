# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# user - title - img - content - created

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField(default=" ")
    img = models.ImageField(upload_to="post_img/")
    created = models.DateTimeField()


    def __str__(self):  # this function to view the post title
        return self.title