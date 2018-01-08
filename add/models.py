from django.db import models

# Create your models here.

# makemigrations add  #让Django知道我们的模型有一些变更
class Test(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    age = models.CharField(max_length=20)