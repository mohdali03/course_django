from django.utils import timezone
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    fee = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"Course = {self.name}, Fees = {self.fee}"

class ExcelFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    
    