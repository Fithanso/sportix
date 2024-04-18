from django.core.validators import MinValueValidator
from django.db import models

from apps.base import models as base_models


class Exercise(base_models.BaseModel):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    type = models.ForeignKey('sports.ExerciseType', on_delete=models.PROTECT, related_name='exercises',
                             verbose_name='Тип')
    difficulty_level = models.ForeignKey('sports.DifficultyLevel', on_delete=models.PROTECT, related_name='exercises',
                                         verbose_name='Уровень сложности')
    duration = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Продолжительность')
    recommended_sets = models.IntegerField(validators=[MinValueValidator(1)],
                                           verbose_name='Рекомендуемый набор подходов')

    def __str__(self):
        return f'{self.title} - {self.type.title}'

    class Meta:
        verbose_name = "упражнение"
        verbose_name_plural = "упражнения"


class ExerciseType(base_models.BaseModel):
    title = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "тип упражнений"
        verbose_name_plural = "типы упражнений"


class DifficultyLevel(base_models.BaseModel):
    title = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "уровень сложности"
        verbose_name_plural = "уровни сложности"
