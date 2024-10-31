from rest_framework import serializers
from User.models import CustomUser, PasswordResetCode


class PasswordRestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.UUIDField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        code = attrs.get("code")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Invalid Email")

        try:
            reset_code = PasswordResetCode.objects.get(user=user, code=code)
        except PasswordResetCode.DoesNotExist:
            raise serializers.ValidationError("Invalid Reset Code")

        if reset_code.is_expired():
            raise serializers.ValidationError("Rest code has expired")

        return attrs

    def save(self):
        email = self.validated_data["email"]
        new_password = self.validated_data["new_password"]

        user = CustomUser.objects.get(email=email)
        user.set_password(new_password)
        user.save()

        PasswordResetCode.objects.filter(user=user).delete()
