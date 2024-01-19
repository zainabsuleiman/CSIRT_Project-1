from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import SignUpSerializer ,UserProfileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class SignUpView(GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []
    @swagger_auto_schema(operation_summary="Create Account",operation_description="this is a function for creating account for  user")
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #class for returing user profile

class UserProfileView(GenericAPIView):
  permission_classes = [IsAuthenticated]
  @swagger_auto_schema(operation_summary="user profile",operation_description="this is a function for returning user  profile")
  def get(self, request):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)