from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User(username='testuser', email='test@example.com', password='password123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')


class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team(name='Team Marvel', members=[])
        self.assertEqual(team.name, 'Team Marvel')


class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity(user='testuser', activity_type='running', duration=30.0, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'running')


class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        entry = Leaderboard(user='testuser', score=100)
        self.assertEqual(entry.score, 100)


class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout(name='Morning Run', description='A quick morning run', duration=30)
        self.assertEqual(workout.name, 'Morning Run')
