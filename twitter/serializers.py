from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import Tweets


class ListTweetsSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = Tweets
        depth = 2
