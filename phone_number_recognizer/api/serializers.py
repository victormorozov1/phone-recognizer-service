import re

from rest_framework import serializers


class PhoneCheckSerializer(serializers.Serializer):
    phone = serializers.CharField()

    def validate_phone(self, value):
        # Validate that the phone number is in MSISDN format:
        # - only digits
        # - starts with '7'
        # - exactly 11 digits long
        if not re.fullmatch(r'7\d{10}', value):
            raise serializers.ValidationError(
                'Phone number must be in MSISDN format, e.g. 79173453223'
            )
        return value
