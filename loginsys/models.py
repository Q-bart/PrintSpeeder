from django.db import models
from django.contrib.auth.models import User
from main.models import Lessons, Exercises

class UserProfile(models.Model):

    user = models.ForeignKey(User)
    current_lesson = models.ForeignKey(Lessons)
    current_exercises = models.ForeignKey(Exercises)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
