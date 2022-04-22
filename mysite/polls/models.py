from django.db import models
import uuid
# Create your models here.
class Maker(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    number = models.IntegerField()
    address = models.CharField(max_length=200)
    Gender_Male = 0
    Gender_Female = 1
    Gender_Choices = [(Gender_Male,'MALE'),(Gender_Female,'female')]
    gender = models.IntegerField(choices=Gender_Choices)

    def __str__(self):
        return self.name

class Tweet(models.Model):
    name = models.ForeignKey(Maker, on_delete=models.CASCADE)    
    tweet = models.TextField(max_length=150)
    date_of_posting = models.DateTimeField(auto_now_add=True)