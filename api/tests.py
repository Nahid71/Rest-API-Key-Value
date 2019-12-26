from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class HomeTests(APITestCase):

    def test_get_values(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.data), 2)

    def test_post_values(self):
        url = reverse('home')
        # { "test_key": "Test value"}
        response = self.client.post(
            url, {"subject": "Test title"}, format='json')
        self.assertEqual(201, response.status_code)

    def test_put_values(self):
        url = reverse('home')
        # { "test_key": "New test value"}
        response = self.client.post(
            url, {"subject": "Test title"}, format='json')
        self.assertEqual(201, response.status_code)
