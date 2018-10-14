from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from twitter.tasks import download_tweets


class MessagesApiView(APIView):

    def post(self, request):

        slack_message = request.data
        if slack_message.get('token') != settings.SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # verification challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,  status=status.HTTP_200_OK)

        # check for # go message
        if slack_message.get('event'):
            event = slack_message.get('event')
            if event.get('text') and settings.SLACK_SEARCH_KEYWORD in event.get('text'):
                download_tweets.delay(screen_name=settings.TWITTER_ACCOUNT_ID)

        return Response(status=status.HTTP_200_OK)