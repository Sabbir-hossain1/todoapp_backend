from rest_framework import serializers
from User.models import CustomUser


class UserModelCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserModelDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserModelRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
