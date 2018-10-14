from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from twitter.serializers import ListTweetsSerializer
from .models import Tweets


class ListTweets(ListAPIView):
    serializer_class = ListTweetsSerializer
    queryset = Tweets.objects.all()
    permission_classes = [AllowAny]
