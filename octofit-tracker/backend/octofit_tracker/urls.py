from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
from . import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboards', views.LeaderboardViewSet)

@api_view(['GET'])
def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev/api/'
    else:
        base_url = request.build_absolute_uri('')
    return Response({
        'teams': base_url + 'teams/',
        'users': base_url + 'users/',
        'activities': base_url + 'activities/',
        'workouts': base_url + 'workouts/',
        'leaderboards': base_url + 'leaderboards/',
    })

@api_view(['GET'])
def root_view(request):
    return Response({
        'message': 'Welcome to Octofit Tracker API',
        'api': request.build_absolute_uri('api/'),
    })

urlpatterns = [
	path('', root_view),
	path('admin/', admin.site.urls),
	path('api/', api_root),
	path('api/', include(router.urls)),
]
