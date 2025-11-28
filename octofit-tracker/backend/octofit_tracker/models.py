from djongo import models
from uuid import uuid4

class Team(models.Model):
    id = models.CharField(primary_key=True, default=lambda: uuid4().hex, editable=False, max_length=32)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.CharField(primary_key=True, default=lambda: uuid4().hex, editable=False, max_length=32)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.CharField(primary_key=True, default=lambda: uuid4().hex, editable=False, max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    id = models.CharField(primary_key=True, default=lambda: uuid4().hex, editable=False, max_length=32)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, default=lambda: uuid4().hex, editable=False, max_length=32)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.team.name} - {self.points}"
