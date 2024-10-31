from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from User.Serializers.PasswordResetRequestSerializer import (
    PasswordResetRequestSerializer,
)
from User.models import CustomUser
from User.utils.password_reset_email_sender import send_password_reset_email


class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(email=serializer.validated_data["email"])
            send_password_reset_email(user)
            return Response(
                {"detail": "Password reset email sent."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
