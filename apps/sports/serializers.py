from rest_framework import serializers

from apps.sports import models as sports_models


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = sports_models.ExerciseType
        fields = '__all__'


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = sports_models.ExerciseType
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = sports_models.Exercise
        fields = '__all__'


class VerboseExerciseSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    difficulty_level = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.type.title

    def get_difficulty_level(self, obj):
        return obj.difficulty_level.title

    class Meta:
        model = sports_models.Exercise
        fields = '__all__'
