from django.conf import settings
from tweepy import API

from twitter.api import TwitterAPI
from zappy.test_helpers import MongoDBTestCase


class TestTwitterAPI(MongoDBTestCase):

    def test_init(self):
        api = TwitterAPI('screen', count=300, max_id='900')
        self.assertEqual('screen', api.screen_name)
        self.assertEqual(300, api.count)
        self.assertEqual('900', api.max_id)
        self.assertIsInstance(api.api, API)

    def test_get_all_tweets(self):
        api = TwitterAPI(settings.TWITTER_ACCOUNT_ID)
        for tweet in api.get_all_tweets():
            self.assertIsNotNone(tweet)
            self.assertIn('id_str', tweet._json)
