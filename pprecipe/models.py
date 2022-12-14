from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.CharField(max_length=200, default='null')

    def __str__(self):
        return self.title