from django.db import models

# Create your models here.


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.text} - {self.author}"
from django.db import models

from django.db import models

class CustomUser(models.Model):
    first_name = models.CharField(max_length=30,default=True)
    last_name = models.CharField(max_length=30,default=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

