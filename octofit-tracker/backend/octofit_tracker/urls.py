from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboards', views.LeaderboardViewSet)

@api_view(['GET'])
def api_root(request):
    return Response({
        'teams': request.build_absolute_uri('teams/'),
        'users': request.build_absolute_uri('users/'),
        'activities': request.build_absolute_uri('activities/'),
        'workouts': request.build_absolute_uri('workouts/'),
        'leaderboards': request.build_absolute_uri('leaderboards/'),
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
