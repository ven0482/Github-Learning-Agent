from rest_framework import serializers
from bson import ObjectId
from .models import User, Team, Activity, Leaderboard, Workout


class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)


class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'password', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']


class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration', 'date']


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'score']


class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'duration']
