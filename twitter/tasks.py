from twitter.api import TwitterAPI
from twitter.models import Tweets
from zappy.celery import app


@app.task(bind=True)
def download_tweets(self, screen_name):
    api = TwitterAPI(screen_name)

    # save tweets
    for tweet in api.get_all_tweets():
        tweet_json = tweet._json
        if Tweets.objects.filter(tweet_id=tweet_json['id_str']).count() > 0:
            continue
        Tweets.create_from_json(tweet_json)
    return True
