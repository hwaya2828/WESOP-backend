import json
import re
import bcrypt
import jwt
import datetime

from django.http  import JsonResponse
from django.views import View

from users.models import User
from my_settings  import SECRET, JWT_ALGORITHM, JWT_ACCESS_TOKEN_DURATION_SECONDS, JWT_REFRESH_TOKEN_DURATION_SECONDS
from users.utils  import login_confirm

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.com$', data['email']) is None:
                return JsonResponse({'message': 'EMAIL_FORM_ERROR'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'ALREADY_EXIT_ERROR'}, status=400)

            if not re.match('^(?=.*[a-zA-Z])(?=.*[0-9])[^ㄱ-ㅎ가-힣ㅏ-ㅣ]{6,10}$', data['password']):
                return JsonResponse({'message': 'PASSWORD_FORM_ERROR'}, status=400)

            if not re.match('^[가-힣a-zA-Z]{1,15}$', data['first_name']):
                return JsonResponse({'message': 'FIRSTNAME_FORM_ERROR'}, status=400)

            if not re.match('^[가-힣a-zA-Z]{1,10}$', data['last_name']):
                return JsonResponse({'message': 'LASTNAME_FORM_ERROR'}, status=400)
            
            hash_password = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt()
            ).decode('utf-8')

            User.objects.create(
                email      = data['email'],
                password   = hash_password,
                first_name = data['first_name'],
                last_name  = data['last_name'],
                phone      = data.get('phone', None)
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError: 
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":'INVALID_USER_ERROR'}, status=400)

            user = User.objects.get(email=data['email'])  

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_USER_ERROR'}, status=400)

            access_token = jwt.encode(
                        {
                            'user_id' : user.id, 
                            'iat'     : datetime.datetime.now().timestamp(),
                            'exp'     : datetime.datetime.now().timestamp() + JWT_ACCESS_TOKEN_DURATION_SECONDS
                        }, 
                        SECRET, 
                        JWT_ALGORITHM
            )

            if user.refresh_token:
                payload = jwt.decode(
                    user.refresh_token,
                    SECRET,
                    JWT_ALGORITHM
                )
                if datetime.datetime.now().timestamp() < payload['exp']:
                    refresh_token = user.refresh_token
            else:
                refresh_token = jwt.encode(
                            {
                                'user_id' : user.id, 
                                'iat'     : datetime.datetime.now().timestamp(),
                                'exp'     : datetime.datetime.now().timestamp() + JWT_REFRESH_TOKEN_DURATION_SECONDS
                            }, 
                            SECRET, 
                            JWT_ALGORITHM
                )
                user.refresh_token = refresh_token
                user.save()

            return JsonResponse({'access_token': access_token, 'refresh_token': refresh_token} ,status=200)

        except KeyError: 
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class UserInformationView(View):
    @login_confirm
    def get(self, request):
        user = request.user

        result = {
            'user_id'         : user.id,
            'user_email'      : user.email,
            'user_first_name' : user.first_name,
            'user_last_name'  : user.last_name,
            'user_email'      : user.email,
            'user_skin_type'  : user.skin_type.name if user.skin_type else None
        }

        return JsonResponse({'result': result}, status = 200)

class ModifyUserInformationView(View):
    @login_confirm
    def patch(self, request, user_id):
        try:
            data = json.loads(request.body)
            user = User.objects.get(id=user_id)
            
            user.first_name = data.get('first_name', user.first_name)
            user.last_name  = data.get('last_name', user.last_name)

            if data.get('password', None):        
                if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                        return JsonResponse({'message': 'NOT_MATCH_PASSWORD_ERROR'}, status=400)
                
                if not re.match('^(?=.*[a-zA-Z])(?=.*[0-9])[^ㄱ-ㅎ가-힣ㅏ-ㅣ]{6,10}$', data['new_password']):
                    return JsonResponse({'message': 'NEW_PASSWORD_FORM_ERROR'}, status=400)
                
                hash_password = bcrypt.hashpw(
                    data['new_password'].encode('utf-8'), bcrypt.gensalt()
                ).decode('utf-8')

                user.password = hash_password
            
            user.birth_day    = data.get('birth_day') if data.get('birth_day') else user.birth_day if user.birth_day else None
            user.skin_type_id = data.get('skin_type_id') if data.get('skin_type_id') else user.skin_type_id if user.skin_type_id else None
            user.update_at    = datetime.datetime.now()
            user.save()

            return JsonResponse({'message':'SUCCESS'}, status=200)
        
        except KeyError: 
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

    @login_confirm
    def delete(self, request, user_id):
        User.objects.get(id=user_id).delete()

        return JsonResponse({'message': 'SUCCESS'}, status=204)