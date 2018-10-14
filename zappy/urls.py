"""zappy URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('slack/', include('slack.urls')),
    path('api/tweets/v1/', include('twitter.urls')),
    path('', include('frontend.urls')),
]
