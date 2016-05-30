from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate

class BasicAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):

        username = request.META.get('HTTP_USERNAME') # get the username request header
        
        if not username: # no username passed in request headers
            return None # authentication did not succeed

        try:
            user = User.objects.get(username=username) # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        return (user, None) # authentication successful