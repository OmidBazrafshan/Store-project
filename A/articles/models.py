from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    item = models.CharField(max_length=120)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    discription = models.TextField()
    is_active = models.BooleanField()
    image=models.ImageField(upload_to="article-images")
    related_user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Sefaresh(models.Model):

    firstname = models.CharField( max_length=120)
    lastname = models.CharField( max_length=120)
    number= models.IntegerField(default=1)
    email = models.EmailField(max_length = 254)
    related_user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.firstname