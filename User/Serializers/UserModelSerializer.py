from rest_framework import serializers
from User.models import CustomUser


class UserModelCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "name", "password", "role"]

    def validate_email(self, value):
        """Validate email and raise custom error code if invalid."""
        if not value or "@" not in value:
            raise serializers.ValidationError(
                {"error_code": 101, "detail": "Invalid email address"}
            )
        return value

    def validate_role(self, value):
        """Validate role and raise custom error code if invalid."""
        valid_roles = [
            CustomUser.Roles.ADMIN,
            CustomUser.Roles.MANAGER,
            CustomUser.Roles.USER,
        ]
        if value not in valid_roles:
            raise serializers.ValidationError(
                {"error_code": 102, "detail": "Invalid role"}
            )
        return value

    def create(self, validated_data):
        # Create user if all validations pass
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data["name"],
            role=validated_data["role"],
        )
        return user


class UserModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password"]


class UserModelDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserModelRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password"]


class UserModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password"]
