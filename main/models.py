from django.db import models

class Lessons(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Exercises(models.Model):
    name = models.IntegerField()
    text = models.TextField(max_length=150)
    lesson = models.ForeignKey(Lessons)

    def __str__(self):
        return str(self.name)
