from django.db import models

# Create your models here.

class Students(models.Model):
    student_id = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    Branch = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name