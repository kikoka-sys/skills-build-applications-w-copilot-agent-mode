from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboards', views.LeaderboardViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
]
