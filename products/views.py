import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models  import Menu, Product, FeatureCategory

class MetaView(View):
    def get(self, request):
        menus = Menu.objects.all()

        results = [
            {
                "menu_name"     : menu.name,
                "menu_id"       : menu.id,
                "category_list" : [
                    {
                        "category_name"              : category.name,
                        "category_id"                : category.id,
                        "category_description_title" : category.description_title if category.description_title else None,
                        "category_description"       : category.description if category.description else None
                    } for category in menu.category_set.all()
                ]
            } for menu in menus
        ]

        return JsonResponse({'result': results}, status=200)

class ProductListView(View):
    def get(self, request):
        menu_id            = request.GET.get('menu_id', None)
        category_id        = request.GET.get('category_id', None)
        skintype_ids       = request.GET.getlist('skintype_id', None)
        productfeature_ids = request.GET.getlist('productfeature_id', None)
        ingredient_ids     = request.GET.getlist('ingredient_id', None)

        q = Q()
        q.add(Q(category__menu_id=menu_id), q.OR)
        q.add(Q(category_id=category_id), q.OR)

        products = Product.objects.filter(q)

        if skintype_ids:
            products = products.filter(Q(feature__in=skintype_ids))
        if productfeature_ids:
            products = products.filter(Q(feature__in=productfeature_ids))
        if ingredient_ids:
            products = products.filter(Q(ingredient__in=ingredient_ids))

        total_results = []

        for product in set(products):
            category = product.category
            menu     = category.menu

            feature_result = [
                {
                    "feature_category_name" : feature_category.name,
                    "features"              : [feature.name for feature in feature_category.feature_set.filter(product=product)]
                } for feature_category in set(FeatureCategory.objects.filter(feature__in=product.feature.all()))
            ]

            results = [
                {
                    "menu_name"                  : menu.name,
                    "menu_id"                    : menu.id,
                    "category_name"              : category.name,
                    "category_id"                : category.id,
                    "category_description_title" : category.description_title,
                    "category_description"       : category.description,
                    "product_name"               : product.name,
                    "product_id"                 : product.id,
                    "product_description"        : product.description,
                    "product_features"           : feature_result,
                    "product_content"            : product.content,
                    "product_content_image_url"  : product.content_image_url,
                    "product_ingredients"        : [ingredient.name for ingredient in product.ingredient.all()],
                    "product_selections"         : [
                        {
                            "size"      : product_selection.size,
                            "price"     : product_selection.price,
                            "image_url" : product_selection.image_url
                        } for product_selection in product.productselection_set.all()
                    ]
                }
            ]

            total_results.append(results)

        return JsonResponse({'result': total_results}, status=200)

class DetailProductView(View):
    def get(self, request, product_id):
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'MESSAGE':'INVALID_PATH'}, status=404)

        product       = Product.objects.get(id=product_id)
        category      = product.category
        menu          = category.menu
        product.count += 1
        product.save()

        results = {
                        "menu_name"                 : menu.name,
                        "menu_id"                   : menu.id,
                        "category_name"             : category.name,
                        "category_id"               : category.id,
                        "product_name"              : product.name,
                        "product_id"                : product.id,
                        "product_description"       : product.description,
                        "product_content"           : product.content,
                        "product_content_image_url" : product.content_image_url,
                        "product_ingredients"       : [ingredient.name for ingredient in product.ingredient.all()],
                        "product_selections"  : [
                            {
                                "size"      : product_selection.size,
                                "price"     : product_selection.price,
                                "image_url" : product_selection.image_url
                            } for product_selection in product.productselection_set.all()
                        ]
        }

        feature_result = [
            {
                "feature_category_name" : feature_category.name,
                "features"              : [feature.name for feature in feature_category.feature_set.filter(product=product)]
            } for feature_category in set(FeatureCategory.objects.filter(feature__in=product.feature.all()))
        ]

        results["product_features"] = feature_result

        return JsonResponse({'result':results}, status=200)