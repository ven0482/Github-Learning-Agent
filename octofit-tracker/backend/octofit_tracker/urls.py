
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = request.build_absolute_uri('/api/')
    return Response({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activities': base_url + 'activities/',
        'leaderboards': base_url + 'leaderboards/',
        'workouts': base_url + 'workouts/',
    })

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
