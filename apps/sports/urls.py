from rest_framework.routers import DefaultRouter

from apps.sports import views as sports_views

app_name = 'sports'
router = DefaultRouter()
router.register(r'exercises', sports_views.ExerciseViewSet, basename='exercise')
router.register(r'exercise-types', sports_views.ExerciseTypeViewSet, basename='exercise_type')
router.register(r'difficulty-levels', sports_views.DifficultyLevelViewSet, basename='difficulty_level')

urlpatterns = []

urlpatterns += router.urls
