from django.db import models

# Create your models here.
class PostFeed(models.Model):
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return str(self.title) + "==>" +str(self.desc)