import json, re, bcrypt, jwt

from datetime     import datetime, timedelta

from django.http  import JsonResponse
from django.views import View

from users.models import User, SkinType
from my_settings  import SECRET

from users.utils  import Authorization_decorator



class UserInformationView(View):
    @Authorization_decorator
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        
        # blank= true에 null 입력 할 수 있도록

        if data['skin_type'] != None :
            info              = data['skin_type']
            skin              = SkinType.objects.get(name=info) if info else '' #get(name=skin_type, '')가능할까?
            skin_id           = skin.id if skin else ''
            user.skin_type_id = skin_id 
            user.save()
        
        if data['address'] != None :
            info = data['address'] 
            user.address = info if info else ''
            user.save()

        return JsonResponse({'MESSAGE': f'update {info}'}, status=200)

# class UserInformationView(View):
#     @Authorization_decorator
#     def post(self, request):
#         data = json.loads(request.body)
        
#         skin_type = data['skin_type']
#         user      = request.user

#         skin              = SkinType.objects.get(name=skin_type)
#         skin_id           = skin.id
#         user.skin_type_id = skin_id 
#         user.save()
        
#         return JsonResponse({'MESSAGE': f'update {key}'}, status=200)

# class SkintypedeleteView(View):
#     @Authorization_decorator
#     def post(self, request):
        
#         user   = request.user
#         users  = User.objects.get(id=user.id)
#         users.skin_type_id = None
#         users.save()
        
#         return JsonResponse({'MESSAGE':'Skintype delete'}, status=200)

# class AddressView(View):
#     @Authorization_decorator
#     def post(self, request):
#         data = json.loads(request.body)

#         address = data['address']
#         user    = request.user

#         user.address = address
#         user.save()

#         return JsonResponse({'MESSAGE':'Address check'}, status=200)

# class AddressdeleteView(View):
#     @Authorization_decorator
#     def post(self, request):
        
#         user   = request.user
#         users  = User.objects.get(id=user.id)
#         users.address = ''
#         users.save()
        
#         return JsonResponse({'MESSAGE':'Address delete'}, status=200)
