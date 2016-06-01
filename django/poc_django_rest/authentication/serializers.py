# -*- coding: utf-8 -*-
from rest_framework import serializers, exceptions
from .models import User, Token

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self):
        self.is_valid()
        return User(**self.validated_data)

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    expires = serializers.CharField()
    user = UserSerializer()

    def create(self):
        if(self.is_valid()):
            user_data = self.validated_data['user']
            self.validated_data.pop('user')
            user = User(**user_data)
            return Token(user=user, **self.validated_data)
        else:
            raise exceptions.AuthenticationFailed('Error in validate permissions')