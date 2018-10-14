from django.urls import path
from twitter.views import ListTweets


urlpatterns = [
    path('list/', ListTweets.as_view(), name="list_all_tweets"),
]