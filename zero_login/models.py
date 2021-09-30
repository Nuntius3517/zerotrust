from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User 

class Profile(models,Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

