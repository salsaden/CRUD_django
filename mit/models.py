from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    school = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.name