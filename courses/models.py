from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class StudyGroup(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    next_at = models.DateTimeField()
