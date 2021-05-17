import json, re, bcrypt, jwt

from datetime     import datetime, timedelta

from django.http  import JsonResponse
from django.views import View

from users.models import User, SkinType
from my_settings  import SECRET


class SignupView(View):

    def post(self,request):
        try:
            data  = json.loads(request.body)

            email        = data['email']
            password     = data['password']
            first_name   = data['first_name']
            last_name    = data['last_name']
            phone_number = data.get('phone', None)

            if (re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.com$', data['email']) is None):
                return JsonResponse({'MESSAGE':'유효하지 않은 Email'}, status=400)

            if (User.objects.filter(email=email).exists()):
                return JsonResponse({'MESSAGE':'이미 존재하는 계정입니다.'}, status=400)

            if (re.match('^[^A-Z]{6,10}$', data['password'])) or (re.match('^[^0-9]{6,10}$', data['password'])):
                return JsonResponse({'MESSAGE':'대문자,숫자,6글자 이상,10글자 이하'}, status=400)

            if not first_name: 
                return JsonResponse({'MESSAGE':'성을 입력하세요.'}, status=400)

            if not last_name:
                return JsonResponse({'MESSAGE':'이름을 입력하세요.'}, status=400)
            
            hash_password=bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            user = User.objects.create(
                email       =email,
                password    =hash_password,
                first_name  =first_name,
                last_name   =last_name,
                phone       =phone_number
                )

            access_token = jwt.encode(
                    {'user_id' : user.id, 'exp':datetime.utcnow()+timedelta(minutes=120)}, 
                    SECRET, 
                    algorithm = 'HS256'
                )

            return JsonResponse({'token':access_token}, status=201)

        except KeyError: 
            return JsonResponse({'MESSAGE':'KeyError'}, status=400)

class LoginView(View):

    def post(self, request):
        data=json.loads(request.body)

        signin_email    = data['email']
        signin_password = data['password']

        if not signin_email and not signin_password:
        	return JsonResponse({"MESSAGE":"KEYERROR"}, status=400)
       
        if not User.objects.filter(email=signin_email).exists():
        	return JsonResponse({"MESSAGE":"INVALID_EMAIL"}, status=400)

        user            = User.objects.get(email=signin_email)         
        hashed_password = user.password.encode('utf-8')

        if not bcrypt.checkpw(signin_password.encode('utf-8'), hashed_password):
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        access_token = jwt.encode(
                    {'user_id' : user.id, 'exp':datetime.utcnow()+timedelta(minutes=120)}, 
                    SECRET, 
                    algorithm = 'HS256'
                )

        return JsonResponse({"token":access_token} ,status=200)