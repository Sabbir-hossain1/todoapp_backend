from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = CustomUser(email=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value
