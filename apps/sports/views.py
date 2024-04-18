from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.sports import models as sports_models
from apps.sports import serializers as sports_serializers
from apps.sports import filters as sports_filters


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary='Получение списка упражнений',
        operation_id='exercise_list'
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Получение объекта упражнения',
        operation_id='exercise_retrieve'
    )
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_summary='Создание объекта упражнения',
        operation_id='exercise_create'
    )
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_summary='Обновление объекта упражнения',
        operation_id='exercise_update'
    )
)
@method_decorator(
    name='partial_update',
    decorator=swagger_auto_schema(
        operation_summary='Частичное обновление объекта упражнения',
        operation_id='exercise_partial_update'
    )
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_summary='Удаление объекта упражнения',
        operation_id='exercise_destroy'
    )
)
@method_decorator(
    name='single_detailed',
    decorator=swagger_auto_schema(
        operation_summary='Получение подробного объекта упражнения',
        operation_id='exercise_detailed_retrieve'
    )
)
class ExerciseViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Exercise
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = sports_models.Exercise
    queryset = sports_models.Exercise.objects.all()
    serializer_class = sports_serializers.ExerciseSerializer
    filterset_class = sports_filters.ExerciseFilter
    lookup_field = 'id'
    ordering = ['-id']

    @action(detail=True, url_path='detailed')
    def single_detailed(self, request, id):
        instance = self.get_object()
        serializer = sports_serializers.VerboseExerciseSerializer(instance)
        return Response(serializer.data)


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary='Получение списка типов упражнений',
        operation_id='exercise_type_list'
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Получение типа упражнений',
        operation_id='exercise_type_retrieve'
    )
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_summary='Создание типа упражнений',
        operation_id='exercise_type_create'
    )
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_summary='Обновление типа упражнений',
        operation_id='exercise_type_update'
    )
)
@method_decorator(
    name='partial_update',
    decorator=swagger_auto_schema(
        operation_summary='Частичное обновление типа упражнений',
        operation_id='exercise_type_partial_update'
    )
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_summary='Удаление типа упражнений',
        operation_id='exercise_type_destroy'
    )
)
class ExerciseTypeViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели ExerciseType
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = sports_models.ExerciseType
    queryset = sports_models.ExerciseType.objects.all()
    serializer_class = sports_serializers.ExerciseTypeSerializer
    lookup_field = 'id'
    ordering = ['-id']


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary='Получение списка уровней сложности',
        operation_id='difficulty_level_list'
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Получение уровня сложности',
        operation_id='difficulty_level_retrieve'
    )
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_summary='Создание уровня сложности',
        operation_id='difficulty_level_create'
    )
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_summary='Обновление уровня сложности',
        operation_id='difficulty_level_update'
    )
)
@method_decorator(
    name='partial_update',
    decorator=swagger_auto_schema(
        operation_summary='Частичное обновление уровня сложности',
        operation_id='difficulty_level_partial_update'
    )
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_summary='Удаление уровня сложности',
        operation_id='difficulty_level_destroy'
    )
)
class DifficultyLevelViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели DifficultyLevel
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = sports_models.DifficultyLevel
    queryset = sports_models.DifficultyLevel.objects.all()
    serializer_class = sports_serializers.DifficultyLevelSerializer
    lookup_field = 'id'
    ordering = ['-id']
    