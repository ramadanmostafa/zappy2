from mongoengine import Document, StringField, BooleanField, IntField


class Tweets(Document):
    tweet_id = StringField(max_length=512)
    user_name = StringField(max_length=512)
    lang = StringField(max_length=512)
    created_at = StringField(help_text='date published')
    text = StringField(max_length=512)
    retweeted = BooleanField(default=False)
    retweet_count = IntField(default=0)

    @staticmethod
    def create_from_json(data):
        tweet_id = data['id_str'] if 'id_str' in data else ''
        user_name = data['user']['name'] if 'user' in data and 'name' in data['user'] else ''
        lang = data['lang'] if 'lang' in data else ''
        created_at = data['created_at'] if 'created_at' in data else ''
        text = data['text'] if 'text' in data else ''
        retweeted = data['retweeted'] if 'retweeted' in data else False
        retweet_count = data['retweet_count'] if 'retweet_count' in data else 0

        return Tweets.objects.create(
            tweet_id=tweet_id, user_name=user_name, lang=lang, created_at=created_at, text=text,
            retweeted=retweeted, retweet_count=retweet_count)
