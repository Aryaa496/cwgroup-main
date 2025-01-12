from django.contrib import admin

# Register your models here.
from .models import Hobby, CustomUser
admin.site.register(Hobby)
admin.site.register(CustomUser)