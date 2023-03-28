from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    email = models.EmailField(max_length=40, validators=[MinLengthValidator(2)])
    feedback = models.TextField()
