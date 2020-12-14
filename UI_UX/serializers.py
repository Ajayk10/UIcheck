from rest_framework import serializers

class PostFeedSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    desc = serializers.CharField(style={'base_template': 'textarea.html'})