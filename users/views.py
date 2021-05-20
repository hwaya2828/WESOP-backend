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
            first_name   = data['firstname']
            last_name    = data['lastname']
            phone_number = data.get('phonenumber', None)

            if (re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.com$', data['email']) is None):
                return JsonResponse({'MESSAGE':'INVALID_EMAIL'}, status=400)

            if (User.objects.filter(email=email).exists()):
                return JsonResponse({'MESSAGE':'EXISTING_USER'}, status=400)

            if not (re.match('^(?=.*[A-Z])(?=.*[0-9])[^ㄱ-ㅎ가-힣ㅏ-ㅣ]{6,10}$', data['password'])):
                return JsonResponse({'MESSAGE':'INVALID_PASSWORD'}, status=400)

            if not (re.match('^[가-힣a-zA-Z]{1,15}$', data['firstname'])):
                return JsonResponse({'MESSAGE':'이름은 1글자 이상,15글자 이하,숫자가 아닌 입력.'}, status=400)

            if not (re.match('^[가-힣a-zA-Z]{1,10}$', data['lastname'])):
                return JsonResponse({'MESSAGE':'성은 1글자 이상,10글자 이하,숫자가 아닌 입력.'}, status=400)
            
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

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

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
            return JsonResponse({'MESSAGE':'INVALID_PASSWORD'}, status=401)

        access_token = jwt.encode(
                    {'user_id' : user.id, 'exp':datetime.utcnow()+timedelta(minutes=120)}, 
                    SECRET, 
                    algorithm = 'HS256'
                )

        return JsonResponse({"token":access_token, "MESSAGE":"SUCCESS"} ,status=200)