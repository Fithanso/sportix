from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.sports import models as sports_models


class ExerciseTests(APITestCase):
    fixtures = ['sports.json', 'accounts.json']

    @classmethod
    def setUpTestData(cls):
        cls.fixture_user = User.objects.get(pk=1)
        cls.user_password = 'nadezhnyi'
        cls.exercise_start_quantity = sports_models.Exercise.objects.count()

    def jwt_auth(self, user):
        auth_request = self.client.post(
            reverse('accounts:token-obtain-pair'),
            {'username': user.username, 'password': self.user_password},
            format='json'
        )
        token = auth_request.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_detailed_retrieve(self):
        last_exercise = sports_models.Exercise.objects.all().latest('id')
        url = reverse('sports:exercise-single-detailed', kwargs={'id': last_exercise.pk})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(sports_models.Exercise.objects.count(), self.exercise_start_quantity)

        self.assertContains(response, 'type')
        self.assertIs(type(response.data.get('type')), str)
        self.assertContains(response, 'difficulty_level')
        self.assertIs(type(response.data.get('difficulty_level')), str)

    def test_user_permission(self):
        last_exercise = sports_models.Exercise.objects.all().latest('id')
        url = reverse('sports:exercise-detail', kwargs={'id': last_exercise.pk})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(sports_models.Exercise.objects.count(), self.exercise_start_quantity)

    def test_list(self):
        url = reverse('sports:exercise-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(sports_models.Exercise.objects.count(), self.exercise_start_quantity)

    def test_create(self):
        self.jwt_auth(user=self.fixture_user)
        url = reverse('sports:exercise-list')
        new_data = {
            "type": 2,
            "difficulty_level": 1,
            "title": "Новое упражнение",
            "description": "хорошее упражнение",
            "duration": 12,
            "recommended_sets": 4
        }

        response = self.client.post(url, new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(sports_models.Exercise.objects.count(), self.exercise_start_quantity + 1)
        self.assertEqual(sports_models.Exercise.objects.all().latest('id').title, new_data['title'])

    def test_delete(self):
        self.jwt_auth(user=self.fixture_user)
        last_exercise = sports_models.Exercise.objects.all().latest('id')
        url = reverse('sports:exercise-detail', kwargs={'id': last_exercise.pk})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(sports_models.Exercise.objects.count(), self.exercise_start_quantity - 1)

    def test_update(self):
        self.jwt_auth(user=self.fixture_user)
        last_exercise = sports_models.Exercise.objects.all().latest('id')
        url = reverse('sports:exercise-detail', kwargs={'id': last_exercise.pk})
        new_data = {
            "difficulty_level": 1,
            "title": "Новое название"
        }

        response = self.client.patch(url, new_data, format='json')
        updated_exercise = sports_models.Exercise.objects.all().latest('id')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_exercise.title, new_data['title'])
        self.assertEqual(updated_exercise.difficulty_level.pk, new_data['difficulty_level'])
        self.assertEqual(last_exercise.description, updated_exercise.description)


class ExerciseTypeTests(APITestCase):
    fixtures = ['sports.json', 'accounts.json']

    @classmethod
    def setUpTestData(cls):
        cls.fixture_user = User.objects.get(pk=1)
        cls.user_password = 'nadezhnyi'
        cls.exercise_type_start_quantity = sports_models.ExerciseType.objects.count()

    def jwt_auth(self, user):
        auth_request = self.client.post(
            reverse('accounts:token-obtain-pair'),
            {'username': user.username, 'password': self.user_password},
            format='json'
        )
        token = auth_request.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_user_permission(self):
        last_exercise_type = sports_models.ExerciseType.objects.all().latest('id')
        url = reverse('sports:exercise_type-detail', kwargs={'id': last_exercise_type.pk})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(sports_models.ExerciseType.objects.count(), self.exercise_type_start_quantity)

    def test_list(self):
        url = reverse('sports:exercise_type-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(sports_models.ExerciseType.objects.count(), self.exercise_type_start_quantity)

    def test_create(self):
        self.jwt_auth(user=self.fixture_user)
        url = reverse('sports:exercise_type-list')
        new_data = {
            "title": "Новый тип",
        }

        response = self.client.post(url, new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(sports_models.ExerciseType.objects.count(), self.exercise_type_start_quantity + 1)
        self.assertEqual(sports_models.ExerciseType.objects.all().latest('id').title, new_data['title'])

    def test_delete(self):
        self.jwt_auth(user=self.fixture_user)
        last_exercise_type = sports_models.ExerciseType.objects.all().latest('id')
        url = reverse('sports:exercise_type-detail', kwargs={'id': last_exercise_type.pk})

        sports_models.Exercise.objects.filter(type=last_exercise_type).delete()
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(sports_models.ExerciseType.objects.count(), self.exercise_type_start_quantity - 1)

    def test_update(self):
        self.jwt_auth(user=self.fixture_user)
        last_exercise_type = sports_models.ExerciseType.objects.all().latest('id')
        url = reverse('sports:exercise_type-detail', kwargs={'id': last_exercise_type.pk})
        new_data = {
            "title": "Новое название"
        }

        response = self.client.patch(url, new_data, format='json')
        updated_exercise_type = sports_models.ExerciseType.objects.all().latest('id')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_exercise_type.title, new_data['title'])
        self.assertEqual(last_exercise_type.pk, updated_exercise_type.pk)


class DifficultyLevelTests(APITestCase):
    fixtures = ['sports.json', 'accounts.json']

    @classmethod
    def setUpTestData(cls):
        cls.fixture_user = User.objects.get(pk=1)
        cls.user_password = 'nadezhnyi'
        cls.difficulty_level_start_quantity = sports_models.DifficultyLevel.objects.count()

    def jwt_auth(self, user):
        auth_request = self.client.post(
            reverse('accounts:token-obtain-pair'),
            {'username': user.username, 'password': self.user_password},
            format='json'
        )
        token = auth_request.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_user_permission(self):
        last_difficulty_level = sports_models.DifficultyLevel.objects.all().latest('id')
        url = reverse('sports:difficulty_level-detail', kwargs={'id': last_difficulty_level.pk})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(sports_models.DifficultyLevel.objects.count(), self.difficulty_level_start_quantity)

    def test_list(self):
        url = reverse('sports:difficulty_level-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(sports_models.DifficultyLevel.objects.count(), self.difficulty_level_start_quantity)

    def test_delete(self):
        self.jwt_auth(user=self.fixture_user)
        last_difficulty_level = sports_models.DifficultyLevel.objects.all().latest('id')
        url = reverse('sports:difficulty_level-detail', kwargs={'id': last_difficulty_level.pk})

        sports_models.Exercise.objects.filter(difficulty_level=last_difficulty_level).delete()
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(sports_models.DifficultyLevel.objects.count(), self.difficulty_level_start_quantity - 1)

    def test_update(self):
        self.jwt_auth(user=self.fixture_user)
        last_difficulty_level = sports_models.DifficultyLevel.objects.all().latest('id')
        url = reverse('sports:difficulty_level-detail', kwargs={'id': last_difficulty_level.pk})
        new_data = {
            "title": "Новое название"
        }

        response = self.client.patch(url, new_data, format='json')
        updated_difficulty_level = sports_models.DifficultyLevel.objects.all().latest('id')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_difficulty_level.title, new_data['title'])
        self.assertEqual(last_difficulty_level.pk, updated_difficulty_level.pk)
