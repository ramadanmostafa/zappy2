from django.test import Client
from django.urls import reverse

from zappy.test_helpers import MongoDBTestCase


class TestIndexView(MongoDBTestCase):
    def test_index(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(200, response.status_code)
