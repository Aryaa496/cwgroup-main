from django.db import models

# Create your models here.
class Hobby(models.Model):
 
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CustomUser(models.Model):
   
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    hobbies = models.ManyToManyField(Hobby, blank=True)  
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.email

class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"
