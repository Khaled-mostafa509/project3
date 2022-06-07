from django.http import request
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import CompanyCustomRegistrationSerializer, PersonCustomRegistrationSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .models import Person,Company,User
from .permissions import IsCompanyUser, IsPersonUser

class CompanySignupView(generics.GenericAPIView):
    serializer_class=CompanyCustomRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "message":"account created successfully"
        })


class PersonSignupView(generics.GenericAPIView):
    serializer_class=PersonCustomRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "message":"account created successfully"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_person':user.is_person
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class PersonOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsPersonUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class CompanyOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsCompanyUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user