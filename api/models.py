from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Hobby model
class Hobby(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        # Use email as the username
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom User Model
class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)  # Optional username field
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)
    
    # Optional relationships to Django's built-in auth system
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    # Telling Django to use email as the username
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name']  # This is a required field when creating superusers

    def __str__(self):
        return self.email

    objects = CustomUserManager() 

    def save(self, *args, **kwargs):
        # Save the user object
        super().save(*args, **kwargs)

        # Ensure hobbies are properly saved (only if they were changed/added)
        if self.hobbies.count() > 0:
            # This checks if any new hobbies were added, and ensures they are saved correctly
            self.hobbies.all()  # Ensure the ManyToMany relationship is updated

        # Call the parent save method again to ensure proper saving
        super().save(*args, **kwargs)
        
 # Link the custom manager

