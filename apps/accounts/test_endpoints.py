from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTests(APITestCase):
    fixtures = ['accounts.json']

    @classmethod
    def setUpTestData(cls):
        cls.fixture_user = User.objects.get(pk=1)
        cls.user_password = 'nadezhnyi'
        cls.wrong_password = 'wrong_pass'

    def test_auth_success(self):
        response = self.client.post(
            reverse('accounts:token-obtain-pair'),
            {'username': self.fixture_user.username, 'password': self.user_password},
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'access')
        self.assertContains(response, 'refresh')

    def test_auth_fail(self):
        response = self.client.post(
            reverse('accounts:token-obtain-pair'),
            {'username': self.fixture_user.username, 'password': self.wrong_password},
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)



