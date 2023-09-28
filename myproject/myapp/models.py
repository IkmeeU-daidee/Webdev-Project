from django.db import models

# Create your models here.    
class Book(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    table = models.IntegerField()
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    