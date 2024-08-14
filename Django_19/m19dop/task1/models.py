from django.db import models
from django.conf import settings
# from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.IntegerField()

    def __str__ (self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    age_limitied = models.BooleanField(True)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
