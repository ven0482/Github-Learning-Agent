from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users (superheroes)
        users = [
            User(username='ironman', email='ironman@avengers.com', password='password123'),
            User(username='captainamerica', email='cap@avengers.com', password='password123'),
            User(username='thor', email='thor@avengers.com', password='password123'),
            User(username='batman', email='batman@dc.com', password='password123'),
            User(username='superman', email='superman@dc.com', password='password123'),
            User(username='wonderwoman', email='wonderwoman@dc.com', password='password123'),
        ]
        for user in users:
            user.save()
        self.stdout.write(self.style.SUCCESS('Created users'))

        # Create teams
        team_marvel = Team(
            name='Team Marvel',
            members=['ironman', 'captainamerica', 'thor']
        )
        team_marvel.save()

        team_dc = Team(
            name='Team DC',
            members=['batman', 'superman', 'wonderwoman']
        )
        team_dc.save()
        self.stdout.write(self.style.SUCCESS('Created teams'))

        # Create activities
        activities = [
            Activity(user='ironman', activity_type='strength training', duration=45.0, date=date(2024, 1, 1)),
            Activity(user='captainamerica', activity_type='running', duration=60.0, date=date(2024, 1, 1)),
            Activity(user='thor', activity_type='hammer throw', duration=30.0, date=date(2024, 1, 2)),
            Activity(user='batman', activity_type='martial arts', duration=90.0, date=date(2024, 1, 2)),
            Activity(user='superman', activity_type='flying', duration=120.0, date=date(2024, 1, 3)),
            Activity(user='wonderwoman', activity_type='sword training', duration=60.0, date=date(2024, 1, 3)),
        ]
        for activity in activities:
            activity.save()
        self.stdout.write(self.style.SUCCESS('Created activities'))

        # Create leaderboard
        leaderboard_entries = [
            Leaderboard(user='superman', score=500),
            Leaderboard(user='wonderwoman', score=450),
            Leaderboard(user='thor', score=420),
            Leaderboard(user='captainamerica', score=400),
            Leaderboard(user='ironman', score=380),
            Leaderboard(user='batman', score=350),
        ]
        for entry in leaderboard_entries:
            entry.save()
        self.stdout.write(self.style.SUCCESS('Created leaderboard entries'))

        # Create workouts
        workouts = [
            Workout(name='Super Strength', description='Intense strength training for maximum power', duration=60),
            Workout(name='Speed Dash', description='High speed running and agility drills', duration=45),
            Workout(name='Endurance Challenge', description='Long distance running to build endurance', duration=90),
            Workout(name='Combat Training', description='Martial arts and combat skills training', duration=75),
            Workout(name='Flight Prep', description='Core and balance training for aerial maneuvers', duration=30),
        ]
        for workout in workouts:
            workout.save()
        self.stdout.write(self.style.SUCCESS('Created workouts'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data'))
