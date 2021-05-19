import json

from django.http      import JsonResponse
from django.views     import View

from products.models  import Product, ProductSelection, FeatureCategory

class PopularProduct(View):
    def get(self, request):
        products = Product.objects.all().order_by('-count')[:5]

        total_results = []

        for product in products:
            category           = product.category
            menu               = category.menu
            ingredients        = product.ingredient.all()
            product_selections = ProductSelection.objects.filter(product_id=product.id)

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
                    "product_ingredients"        : [ingredient.name for ingredient in ingredients],
                    "product_selections"         : [
                        {
                            "size"      : product_selection.size,
                            "price"     : product_selection.price,
                            "image_url" : product_selection.image_url
                        } for product_selection in product_selections
                    ]
                }
            ]

            total_results.append(results)

        return JsonResponse({'result': total_results}, status=200)