import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models  import Menu, Category, Product, FeatureCategory

class MetaView(View):
    def get(self, request):
        results = [
            {
                "menu_id"    : menu.id,
                "menu_name"  : menu.name,
                "categories" : [
                    {
                        "category_id"                : category.id,
                        "category_name"              : category.name,
                        "category_description_title" : category.description_title if category.description_title else None,
                        "category_description"       : category.description if category.description else None
                    } for category in menu.category_set.all()
                ]
            } for menu in Menu.objects.all()
        ]

        return JsonResponse({'result': results}, status=200)

class ProductListView(View):
    def get(self, request):
        menu_id     = request.GET.get('menu_id', None)
        category_id = request.GET.get('category_id', None)
        search_name = request.GET.get('search_name', None)

        skin_type_ids  = request.GET.getlist('skin_type_id', None)
        texture_ids    = request.GET.getlist('texture_id', None)
        scent_ids      = request.GET.getlist('scent_id', None)
        ingredient_ids = request.GET.getlist('ingredient_id', None)

        q = Q()

        if menu_id:
            q.add(Q(category__menu_id=menu_id), q.OR)
        if category_id:
            q.add(Q(category_id=category_id), q.OR)
        if search_name:
            q.add(Q(name__contains=search_name), q.OR)

        products = Product.objects.filter(q)

        if skin_type_ids:
            products = products.filter(feature__in=skin_type_ids).distinct()
        if texture_ids:
            products = products.filter(feature__in=texture_ids).distinct()
        if scent_ids:
            products = products.filter(feature__in=scent_ids).distinct()
        if ingredient_ids:
            products = products.filter(ingredient__in=ingredient_ids).distinct()

        total_results = [
            {
                "categories" : [
                        {
                            "category_id"                : category.id,
                            "category_name"              : category.name,
                            "category_description_title" : category.description_title if category.description_title else None,
                            "category_description"       : category.description if category.description else None
                        } for category in Category.objects.filter(id__in=[product.category.id for product in products]).distinct()
                ]
            }
        ]

        for product in products:
            feature_result = [
                {
                    "feature_category_name" : feature_category.name,
                    "features"              : [feature.name for feature in feature_category.feature_set.filter(product=product)]
                } for feature_category in FeatureCategory.objects.filter(feature__in=[feature.id for feature in product.feature.all()]).distinct()
            ]

            results = [
                {
                    "category_id"                : product.category.id,
                    "category_name"              : product.category.name,
                    "product_id"                 : product.id,
                    "product_name"               : product.name,
                    "product_summary"            : product.summary,
                    "product_thumbnail_url"      : product.thumbnail_url,
                    "product_features"           : feature_result,
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

class ProductDetailView(View):
    def get(self, request, product_id):

        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'message': 'DOES_NOT_EXIST_ERROR'}, status=404)

        product       = Product.objects.get(id=product_id)
        product.count += 1
        product.save()

        results = {
                        "menu_name"                 : product.category.menu.name,
                        "category_name"             : product.category.name,
                        "product_id"                : product.id,
                        "product_name"              : product.name,
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
            } for feature_category in FeatureCategory.objects.filter(feature__in=product.feature.all()).distinct()
        ]

        results["product_features"] = feature_result

        return JsonResponse({'result': results}, status=200)

class PopularProducts(View):
    def get(self, request):
        COUNT_RANKING = 5
        products      = Product.objects.all().order_by('-count')[:COUNT_RANKING]

        total_results = [
            {
                "categories" : [
                        {
                            "category_id"                : category.id,
                            "category_name"              : category.name,
                            "category_description_title" : category.description_title if category.description_title else None,
                            "category_description"       : category.description if category.description else None
                        } for category in Category.objects.filter(id__in=[product.category.id for product in products]).distinct()
                ]
            }
        ]

        for product in products:
            feature_result = [
                {
                    "feature_category_name" : feature_category.name,
                    "features"              : [feature.name for feature in feature_category.feature_set.filter(product=product)]
                } for feature_category in FeatureCategory.objects.filter(feature__in=[feature.id for feature in product.feature.all()]).distinct()
            ]

            results = [
                {
                    "category_id"                : product.category.id,
                    "category_name"              : product.category.name,
                    "product_id"                 : product.id,
                    "product_name"               : product.name,
                    "product_summary"            : product.summary,
                    "product_thumbnail_url"      : product.thumbnail_url,
                    "product_features"           : feature_result,
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