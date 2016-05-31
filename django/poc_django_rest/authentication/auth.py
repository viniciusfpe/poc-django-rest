import http.client
from django.contrib.auth import authenticate
from django.utils.six import BytesIO
from rest_framework import exceptions
from rest_framework import authentication
from rest_framework.parsers import JSONParser
from .serializers  import TokenSerializer

class BasicAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION')
        try:
            token = self.get_token(authorization)            
        except:
            raise exceptions.AuthenticationFailed('No such user')

        return (token.user, None)

    def get_token(self, token):
        conn = http.client.HTTPConnection('192.168.50.245:8080')
        conn.set_debuglevel(0)
        conn.request(method='GET', url='/token?token='+token, headers={'Content-Type': 'application/json'})
        try:
            response = conn.getresponse()
            response_status  = response.status
            response_body = response.read()
        except(Exception, e):
            raise Exception('Connection Error: %s' % e)
        finally:
            conn.close()

        if(response_status != http.client.UNAUTHORIZED):
            stream = BytesIO(response_body)
            data = JSONParser().parse(stream)   
            print(data)     
            serializer = TokenSerializer(data=data)
            return serializer.create()
        else:
            raise Exception