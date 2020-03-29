from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expence(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

