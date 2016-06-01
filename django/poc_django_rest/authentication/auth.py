# -*- coding: utf-8 -*-
import http.client, urllib.parse
from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.six import BytesIO
from rest_framework import authentication, exceptions
from rest_framework.parsers import JSONParser
from .serializers  import TokenSerializer


class BasicAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION')
        try:
            token = self.get_token(authorization)            
        except exceptions.AuthenticationFailed as e:
            raise exceptions.AuthenticationFailed(e)

        return (token.user, None)

    def get_token(self, token):
        try:
            conn = http.client.HTTPConnection(settings.WITWICKY['HOST'])
            conn.request(method=settings.WITWICKY['METHOD'], url=settings.WITWICKY['PATH'] + '?' + urllib.parse.urlencode({'token': token}), headers={'Content-Type': 'application/json'})
            response = conn.getresponse()
            response_status  = response.status
            response_body = response.read()
        except:
            raise exceptions.AuthenticationFailed('Token not set')
        finally:
            conn.close()

        if(response_status == http.client.OK):
            try:
                stream = BytesIO(response_body)
                data = JSONParser().parse(stream) 
                print(data) 
                serializer = TokenSerializer(data=data)
                return serializer.create()
            except exceptions.AuthenticationFailed as e:
                raise exceptions.AuthenticationFailed(e)
        else:
            raise exceptions.AuthenticationFailed('Token invalid')