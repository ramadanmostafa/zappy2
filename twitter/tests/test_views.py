from django.urls import reverse
from django.test import Client

from twitter.models import Tweets
from zappy.test_helpers import MongoDBTestCase


class TestListTweets(MongoDBTestCase):
    def setUp(self):
        super().setUp()
        Tweets.objects.create(
            tweet_id='id1', user_name='user1', lang='eng', created_at='test', text='text1',
            retweeted=True, retweet_count=20)
        Tweets.objects.create(
            tweet_id='id2', user_name='user1', lang='eng', created_at='test', text='text13',
            retweeted=True, retweet_count=90)
        Tweets.objects.create(
            tweet_id='id3', user_name='user1', lang='eng', created_at='test3', text='text3')

    def test_get(self):
        client = Client()
        response = client.get(reverse('list_all_tweets'), content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(response.data))
        self.assertEqual('id1', response.data[0]['tweet_id'])
        self.assertEqual('id2', response.data[1]['tweet_id'])
        self.assertEqual('id3', response.data[2]['tweet_id'])