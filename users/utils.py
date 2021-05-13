import  jwt
import  json
import  requests

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings            import SECRET
from users.models           import User

def decorator(func):

    def wrapper(self, request, *arg, **kwarg):
        try:
                access_token = request.headers.get('Authorization',None) 
                payload      = jwt.decode(
                    access_token, 
                    SECRET, 
                    algorithm = 'HS256' #PyJWT == 1.7.1, -s 붙여도 됨
                    ) 
                
                user         = User.objects.get(id=payload['user_id']) 
                request.user = user 

        except jwt.exceptions.ExpiredSignatureError:
                return JsonResponse({'message':'Token has expired'}, status=401)

        except jwt.exceptions.DecodeError:
                return JsonResponse({'message':'INVALID_TOKEN'},status=401)

        except User.DoesNotExist:
                return JsonResponse({'message':'INVALID_USER'},status=401)

        return func(self, request) #*arg,*kwargs is not defined error 발생? wrapper에서는 왜 안발생하는 걸까?
							
    return wrapper