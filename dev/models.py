from django.db import models
class Useradmin(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    image= models.ImageField(upload_to="image/", default=0)


class Post(models.Model):
    title=models.CharField(max_length=100)
    content= models.TextField()

    def __str__(self):
        return self.title