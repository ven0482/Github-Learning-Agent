from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data safely
        for model in [Activity, Leaderboard, Workout, User, Team]:
            objs = model.objects.all()
            for obj in objs:
                if getattr(obj, 'pk', None):
                    obj.delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = []
        users.append(User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'))
        users.append(User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel'))
        users.append(User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'))
        users.append(User.objects.create(name='Batman', email='batman@dc.com', team='DC'))

        # Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=75)
        Leaderboard.objects.create(team=dc, points=80)

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for superheroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Strength and flexibility', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
