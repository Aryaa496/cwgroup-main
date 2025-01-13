from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Hobby(models.Model):
 
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = None 
    password=None
   
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)  
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups', 
        blank=True,
        # help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions', 
        blank=True,
        # help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name'] 
    


    def __str__(self):
        return self.email

class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"