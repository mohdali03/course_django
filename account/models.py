from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here. 

class CustomUser(AbstractUser):
    user_type_choices = (('teacher', 'Teacher'),
                 ('student', 'Student'))
    user_type = models.CharField(
        max_length=10,
        choices=user_type_choices,
        default="student",
        help_text="Designates whether the user is a teacher or student."
        
    )
    
    def __str__(self):
        return self.username