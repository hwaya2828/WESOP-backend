import jwt
import json
import requests
import datetime

from django.http  import JsonResponse

from my_settings  import SECRET, JWT_ALGORITHM, JWT_ACCESS_TOKEN_DURATION_SECONDS
from users.models import User

def login_confirm(original_function):

    def wrapper(self, request, *arg, **kwarg):
        try:
            access_token = request.headers.get('AccessToken', None)

            if not access_token:
                return JsonResponse({'message': 'LOGIN_REQUIRED'}, status=401)

            payload = jwt.decode(
                access_token, 
                SECRET, 
                JWT_ALGORITHM 
            ) 

            user         = User.objects.get(id=payload['user_id']) 
            request.user = user

        except jwt.exceptions.ExpiredSignatureError:
            refresh_token = request.headers.get('RefreshToken')

            payload = jwt.decode(
                refresh_token, 
                SECRET, 
                JWT_ALGORITHM 
                ) 

            user = User.objects.get(id=payload['user_id'])

            if user.refresh_token == refresh_token:
                if datetime.datetime.now().timestamp() < payload['exp']:
                    access_token = jwt.encode(
                            {
                                'user_id' : user.id, 
                                'iat'     : datetime.datetime.now().timestamp(),
                                'exp'     : datetime.datetime.now().timestamp() + JWT_ACCESS_TOKEN_DURATION_SECONDS
                            }, 
                            SECRET, 
                            JWT_ALGORITHM
                )
                else:
                    return JsonResponse({'message': 'REFRESH_TOKEN_EXPIRED'},status=401)

            return JsonResponse({'access_token': access_token}, status=200)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'},status=400)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'},status=400)

        return original_function(self, request,*arg, **kwarg) 

    return wrapper