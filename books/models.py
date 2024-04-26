from django.db import models

# Create your models here.


class books(models.Model):
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    ISBN=models.CharField(max_length=50)
    category = models.TextField()

    def __str__(self):
        return self.title