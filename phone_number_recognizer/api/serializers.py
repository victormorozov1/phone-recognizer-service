from rest_framework import serializers

class PhoneCheckSerializer(serializers.Serializer):
    phone = serializers.CharField()
