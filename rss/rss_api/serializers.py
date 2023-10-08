from rest_framework import serializers
from .models import RSSFeed, SelectedFeed

class RSSFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSSFeed
        fields = ('id', 'title', 'link', 'description', 'pub_date')

class SelectedFeedSerializer(serializers.ModelSerializer):
    rss_feed = RSSFeedSerializer()  # Serializar el objeto RSSFeed dentro de SelectedFeed

    class Meta:
        model = SelectedFeed
        fields = ('id', 'rss_feed', 'selected')
