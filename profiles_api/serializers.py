from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialzes a name field for testing out our APIview"""
    name = serializers.CharField(max_length=10)
