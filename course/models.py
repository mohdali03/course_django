from django.db import models

# Create your models here.
class Course(models.Model):
    
    name = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    fee = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Course = {self.name}, Fees = {self.fee}"
    