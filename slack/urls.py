from django.urls import path
from slack.views import MessagesApiView


urlpatterns = [
    path('messages/', MessagesApiView.as_view(), name="slack_messages"),
]