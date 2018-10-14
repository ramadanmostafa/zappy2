from twitter.models import Tweets
from zappy.test_helpers import MongoDBTestCase


class TestTweetsModel(MongoDBTestCase):

    def test_create_from_json_empty(self):
        tweet = Tweets.create_from_json({})
        self.assertEqual('', tweet.tweet_id)
        self.assertEqual('', tweet.user_name)
        self.assertEqual('', tweet.lang)
        self.assertEqual('', tweet.created_at)
        self.assertEqual('', tweet.text)
        self.assertFalse(tweet.retweeted)
        self.assertEqual(0, tweet.retweet_count)

    def test_create_from_json_all(self):
        data = {
            'id_str': 'id_str',
            'user': {'name': 'name'},
            'lang': 'lang',
            'created_at': 'created_at',
            'text': 'text',
            'retweeted': True,
            'retweet_count': 50,
        }
        tweet = Tweets.create_from_json(data)
        self.assertEqual('id_str', tweet.tweet_id)
        self.assertEqual('name', tweet.user_name)
        self.assertEqual('lang', tweet.lang)
        self.assertEqual('created_at', tweet.created_at)
        self.assertEqual('text', tweet.text)
        self.assertTrue(tweet.retweeted)
        self.assertEqual(50, tweet.retweet_count)
