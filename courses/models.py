from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StudyGroup(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    next_at = models.DateTimeField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:detail", kwargs={"pk": self.pk})
