from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid 

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    avg_mark = models.FloatField()
    secret_value = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name