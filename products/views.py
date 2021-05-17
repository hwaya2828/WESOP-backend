import json

from django.http     import JsonResponse
from django.views    import View

from products.models import Product, ProductSelection, FeatureCategory

class DetailProductView(View):
    def get(self, request, product_id):
        if product_id and Product.objects.filter(id=product_id).exists():
            product = Product.objects.get(id=product_id)
        else:
            return JsonResponse({'MESSAGE':'INVALID_PATH'}, status=404)

        category           = product.category
        menu               = category.menu
        ingredients        = product.ingredient.all()
        product_selections = ProductSelection.objects.filter(product_id=product.id)
        product.count      += 1
        # product.save() 프로젝트 완성되면 카운트 쌓을 예정입니다 :)

        results = {
                        "menu_name"                : menu.name,
                        "menu_id"                  : menu.id,
                        "category_name"            : category.name,
                        "category_id"              : category.id,
                        "product_name"             : product.name,
                        "product_id"               : product.id,
                        "description"              : product.description,
                        "content"                  : product.content,
                        "content_image_url"        : product.content_image_url,
                        "ingredient_result"        : [ingredient.name for ingredient in ingredients],
                        "product_selection_result" : [
                            {
                                "size"      : product_selection.size,
                                "price"     : product_selection.price,
                                "image_url" : product_selection.image_url
                            } for product_selection in product_selections 
                        ]
        }

        features            = product.feature.all()
        feature_category_id = set([feature.feature_category_id for feature in features])
        feature_result      = []
        for id in feature_category_id:
            feature_category_name = FeatureCategory.objects.get(id=id).name
            feature_detail_result = [i.name for i in features.filter(feature_category_id=id)]
            feature_result.append(
                {
                    "feature_category_name" : feature_category_name,
                    "features"              : feature_detail_result
                }
            )
        results["feature"] = feature_result

        return JsonResponse({'result':results}, status=200)
