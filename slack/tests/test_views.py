from unittest.mock import patch

from django.test import Client
from django.urls import reverse
from django.conf import settings

from zappy.test_helpers import MongoDBTestCase


class TestIndexView(MongoDBTestCase):

    def test_invalid_token(self):
        client = Client()
        response = client.post(reverse('slack_messages'), data={"token": 'token'}, content_type='application/json')
        self.assertEqual(403, response.status_code)

    def test_verification_challenge(self):
        data = {"token": settings.SLACK_VERIFICATION_TOKEN, 'type': 'url_verification'}
        client = Client()
        response = client.post(reverse('slack_messages'), data=data, content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertIn('type', response.data)
        self.assertIn('token', response.data)
        self.assertEqual('url_verification', response.data['type'])

    @patch('slack.views.download_tweets', autospec=True)
    def test_valid_task_not_called(self, task):
        data = {"token": settings.SLACK_VERIFICATION_TOKEN, 'event': {'text': 'test'}}
        client = Client()
        response = client.post(reverse('slack_messages'), data=data, content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertFalse(task.delay.called)

    @patch('slack.views.download_tweets', autospec=True)
    def test_valid_task_called(self, task):
        data = {
            "token": settings.SLACK_VERIFICATION_TOKEN,
            'event': {'text': ' {} test'.format(settings.SLACK_SEARCH_KEYWORD)}
        }
        client = Client()
        response = client.post(reverse('slack_messages'), data=data, content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertTrue(task.delay.called)
