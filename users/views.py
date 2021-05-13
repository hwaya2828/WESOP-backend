import json, re, bcrypt, jwt

from datetime     import datetime, timedelta

from django.http  import JsonResponse
from django.views import View

from users.models import User, SkinType
from my_settings  import SECRET
from users.utils  import decorator


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

        user            = User.objects.get(email=signin_email)         
        hashed_password = user.password.encode('utf-8')
            
        if not signin_email and not signin_password:
        	return JsonResponse({"messege":"KEYERROR"}, status=400)
       
        if not User.objects.filter(email=signin_email).exists():
        	return JsonResponse({"messege":"INVALID_EMAIL"}, status=400)

        if not bcrypt.checkpw(signin_password.encode('utf-8'), hashed_password):
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        access_token = jwt.encode(
                    {'user_id' : user.id, 'exp':datetime.utcnow()+timedelta(minutes=120)}, 
                    SECRET, 
                    algorithm = 'HS256'
                )
        access_token = access_token.decode('utf-8')

        return JsonResponse({"token":access_token} ,status=200)    

# class LogoutView(View):
#     @decorator
#     def logout(self,request):
#         # json으로 받아서, token=''으로 변경, front에 return하면 front에서 token=0일시 token 삭제 logic 있으면 어떨까?

#         return redirect(본문 url?)

class SkintypeView(View):
    @decorator
    def post(self, request):
        data = json.loads(request.body)
        
        skin_type = data['skin_type']
        user      = request.user

        skin              = SkinType.objects.get(name=skin_type)
        skin_id           = skin.id
        user.skin_type_id = skin_id 
        user.save()
        # User.objects.get(id=user_id).update(skin_type_id=skin_id)

        # skin_type_id 와 skin_type 일 때 차이?
        # 역참조 방식 생각해보기, skin.User_set.create(user.skin_type_id=skin.id)
        return JsonResponse({'MESSAGE':user.skin_type_id}, status=200)

class AddressView(View):
    @decorator
    def post(self, request):
        data = json.loads(request.body)

        address = data['address']
        user    = request.user

        # User.objects.get(id=user_id).update(address = address)
        user.address = address
        user.save()

        return JsonResponse({'MESSAGE':'Adress check'}, status=200)

