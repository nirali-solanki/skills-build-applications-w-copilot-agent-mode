
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Use PyMongo to drop collections directly
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        for collection in ['activities', 'leaderboard', 'users', 'teams', 'workouts']:
            db[collection].drop()
        client.close()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Heavy lifting and power moves', suggested_for='DC'),
            Workout.objects.create(name='Agility Training', description='Speed and flexibility drills', suggested_for='Marvel'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Bench Press', duration=60, date=timezone.now())
        Activity.objects.create(user=users[3], type='Flight', duration=30, date=timezone.now())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
