from django.db import models

# Create your models here.

class MyDataBase(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    is_male = models.BooleanField()
    class Meta:
        db_table = 'personal_info'
