from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"Предмет: {self.title} ({self.description})\n"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"\n{self.name} {self.last_name}, {self.subject}"

class ClassRoom(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.year} \n"

class Student(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.last_name}, {self.classroom}\n"

class Schedule(models.Model):
    day_of_week = models.CharField(max_length=20)
    hour_of_start = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day_of_week}, {self.hour_of_start} - {self.subject}, {self.classroom} ({self.teacher})"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student} отримала {self.grade} з предмету {self.subject} ({self.date}) \n"
