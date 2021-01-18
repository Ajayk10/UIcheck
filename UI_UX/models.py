from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime,date

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name= 'post_feed')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " - " +str(self.author) + "----->" + str(self.likes)

    def get_absolute_url (self):
        return reverse('article',args=str(self.id))


