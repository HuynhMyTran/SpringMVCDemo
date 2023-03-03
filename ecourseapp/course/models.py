from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass


class Catergory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name