import json, re, bcrypt, jwt

from datetime     import datetime, timedelta

from django.http  import JsonResponse
from django.views import View

from users.models import User, SkinType
from my_settings  import SECRET

from users.utils  import decorator

class CartaddView(View):
    def Post(self, request):
        return JsonResponse({'MESSAGE':'Product add in cart.'})

class CartdeleteView(View):
    def Post(self, request):
        return JsonResponse({'MESSAGE':'Product deleted from cart.'})

class CartquantityView(View):
    def Post(self, request):
        return JsonResponse({'MESSAGE':'Product quantity in cart updated.'})

class CartcheckView(View):
    def Post(self, request):
        return JsonResponse({'MESSAGE':'SUCCESS'})

class OrdercheckView(View):
    def Post(self, request):
        return JsonResponse({'MESSAGE':'SUCCESS'})