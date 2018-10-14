import tweepy

from django.conf import settings


class TwitterAPI(object):

    def __init__(self, screen_name, count=200, max_id=None):
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_KEY, settings.TWITTER_ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.screen_name = screen_name
        self.count = count
        self.max_id = max_id

    def get_all_tweets(self):
        while True:
            new_tweets = self.api.user_timeline(screen_name=self.screen_name, count=self.count, max_id=self.max_id)
            if len(new_tweets) < 1:
                return
            for tweet in new_tweets:
                yield tweet

            self.max_id = new_tweets[-1].id - 1
