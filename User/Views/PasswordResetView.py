from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from User.Serializers.PasswordResetSerializer import PasswordRestSerializer


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordRestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Password reset successful."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
