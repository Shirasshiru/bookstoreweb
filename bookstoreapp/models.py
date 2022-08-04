from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')
    desc=models.TextField()
    price=models.IntegerField(max_length=250)
    author=models.CharField(max_length=250)

    def __str__(self):
        return self.name