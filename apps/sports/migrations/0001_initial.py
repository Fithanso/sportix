# Generated by Django 5.0.4 on 2024-04-17 22:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_dttm', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'уровень сложности',
                'verbose_name_plural': 'уровни сложности',
            },
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_dttm', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'тип упражнений',
                'verbose_name_plural': 'типы упражнений',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_dttm', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Продолжительность')),
                ('recommended_sets', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Рекомендуемый набор подходов')),
                ('difficulty_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='sports.difficultylevel', verbose_name='Уровень сложности')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='sports.exercisetype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'упражнение',
                'verbose_name_plural': 'упражнения',
            },
        ),
    ]