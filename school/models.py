from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}, {self.description}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.last_name}, {self.subject}"

class ClassRoom(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.year}"

class Student(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.last_name}, {self.classroom}"
