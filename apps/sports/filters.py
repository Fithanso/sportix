from django_filters import rest_framework as filters

from apps.sports import models as sports_models


class ExerciseFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='type', lookup_expr='pk')
    difficulty_level = filters.CharFilter(field_name='difficulty_level', lookup_expr='pk')

    class Meta:
        model = sports_models.Exercise
        fields = [
            'type',
            'difficulty_level',
        ]
