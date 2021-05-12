import json, re, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models  import User, SkinType
from my_settings  import SECRET


class SignupView(View):

    def post(self,request):
        try:
            data  = json.loads(request.body)

            email       = data['email']
            password    = data['password']
            first_name  = data['first_name']
            last_name   = data['last_name']
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
                phone = phone_number
                )

            access_token = jwt.encode(
                    {'user_id' : user.id}, 
                    SECRET, 
                    algorithm = 'HS256'
                )

            return JsonResponse({'token':access_token}, status=201)

        except KeyError: 
            return JsonResponse({'MESSAGE':'KeyError'}, status=400)