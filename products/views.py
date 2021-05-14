import json

from django.http     import JsonResponse
from django.views    import View

from products.models import Menu

class MetaView(View):
    def get(self, request):
        menus = Menu.objects.all()

        results = [{
                "menu_name"     : menu.name,
                "category_list" : [{
                                "category_name"     : category.name,
                                "description_title" : category.description_title if category.description_title else None, 
                                "description"       : category.description if category.description else None 
                                } for category in menu.category_set.all()]
                } for menu in menus]

        return JsonResponse({'result': results}, status=200)
