from django.contrib import admin

from apps.sports import models as sports_models


@admin.register(sports_models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'type', 'difficulty_level', 'duration', 'recommended_sets', 'created_dttm',
              'updated_dttm']
    list_display = ['id', 'title', 'type', 'difficulty_level', 'duration', 'recommended_sets']
    list_display_links = ['id', ]
    readonly_fields = ['created_dttm', 'updated_dttm']


@admin.register(sports_models.ExerciseType)
class ExerciseTypeAdmin(admin.ModelAdmin):
    fields = ['title', 'created_dttm', 'updated_dttm']
    list_display = ['id', 'title']
    list_display_links = ['id', ]
    readonly_fields = ['created_dttm', 'updated_dttm']


@admin.register(sports_models.DifficultyLevel)
class DifficultyLevelAdmin(admin.ModelAdmin):
    fields = ['title', 'created_dttm', 'updated_dttm']
    list_display = ['id', 'title']
    list_display_links = ['id', ]
    readonly_fields = ['created_dttm', 'updated_dttm']