from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from accounts.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.contrib.auth import (
    authenticate as django_authenticate,
    login as django_login,
    logout as django_logout,
)
from accounts.api.serializers import SignupSerializer, LoginSerializer
from accounts.api.serializers import SignupSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AccountViewSet(viewsets.ViewSet):
    permissions_classes = (AllowAny,)
    serializers_class = SignupSerializer

    @action(methods=['POST'], detail = False)
    def signup(self, request):
        """
        使用 username, email, password 进行注册
        注册中用到的 SignupSerializer 在 accounts/api/serializers.py 中：
        """
        # 不太优雅的写法
        # username = request.data.get('username')
        # if not username:
        # return Response("username required", status=400)
        # password = request.data.get('password')
        # if not password:
        # return Response("password required", status=400)
        # if User.objects.filter(username=username).exists():
        # return Response("password required", status=400)
        serializer = SignupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'success': False
                'message': "Please check input",
                'error': serializer.errors,

            }, status=400)
