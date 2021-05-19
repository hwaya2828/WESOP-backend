import json, re, bcrypt, jwt

from datetime     import datetime, timedelta

from django.http  import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from users.models import User, SkinType
from my_settings  import SECRET

from users.utils  import Authorization_decorator

class UserInformationView(View):
    @Authorization_decorator
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        information = 'Nothing'

        try:
            if data['skin_type'] != '' :
                information       = data['skin_type']
                skin              = SkinType.objects.get(name=information) if information!='empty' else '' 
                skin_id           = skin.id if skin else ''
                user.skin_type_id = skin_id 
                user.save()
            
            if data['address'] != '' :
                information = data['address'] 
                user.address = information if information != 'empty' else ''
                user.save()

            return JsonResponse({'MESSAGE': f'update {information}'}, status=200)
        
        except SkinType.DoesNotExist:
            return JsonResponse({'MESSAGE':'Invalid skintype request'}, status=400)