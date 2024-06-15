from django.db import models

# Create your models here.
class blogPost(models.Model):
    title= models.CharField(max_length=99)
    content = models.TextField()
    published_date = models.DateTimeField( auto_now_add=True)
    author= models.CharField(max_length=99)
    def __str__(self):
        return self.title