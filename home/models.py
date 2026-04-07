from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    absences = models.IntegerField(default=0)
    contacts = models.CharField(default="No contact", max_length=200)


class Classes(models.Model):
    class_number = models.CharField(max_length=100, default="0", unique=True)