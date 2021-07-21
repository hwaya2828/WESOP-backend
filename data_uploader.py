import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wesop.settings")
django.setup()

from products.models import *
from users.models    import *
from orders.models   import *

big_product_image1 = "https://i.postimg.cc/zvdQ5YxB/big-product1.png"
big_product_image2 = "https://i.postimg.cc/bvBHzNh4/big-product2.png"
big_product_image3 = "https://i.postimg.cc/8kWBSSnn/big-product3.png"
big_product_image4 = "https://i.postimg.cc/k4S8qQwt/big-product4.png"
big_product_image5 = "https://i.postimg.cc/PqpvQWgF/big-product5.png"
big_product_image6 = "https://i.postimg.cc/xjyJ5TZY/big-product6.png"

small_product_image1 = "https://i.postimg.cc/j2sjmP1T/product1.png"
small_product_image2 = "https://i.postimg.cc/pdzXdsbx/product2.png"
small_product_image3 = "https://i.postimg.cc/brCq5Mb0/product3.png"
small_product_image4 = "https://i.postimg.cc/X7PVcRn4/product4.png"
small_product_image5 = "https://i.postimg.cc/vBGMZMtL/product5.png"
small_product_image6 = "https://i.postimg.cc/pVGxRwhz/product6.png"

content_image1 = "https://i.postimg.cc/D0rSrHC1/contentimg1.jpg"
content_image2 = "https://i.postimg.cc/5NJY490g/contentimg2.jpg"
content_image3 = "https://i.postimg.cc/Xq8Xph7q/contentimg3.jpg"
content_image4 = "https://i.postimg.cc/kXTBCkph/contentimg4.jpg"

products = Product.objects.all()

for product in products:
    if product.id % 6 == 1:
        product.thumbnail_url = big_product_image1
        product.save()
    if product.id % 6 == 2:
        product.thumbnail_url = big_product_image6
        product.save()
    if product.id % 6 == 3:
        product.thumbnail_url = big_product_image3
        product.save()
    if product.id % 6 == 4:
        product.thumbnail_url = big_product_image4
        product.save()
    if product.id % 6 == 5:
        product.thumbnail_url = big_product_image5
        product.save()
    if product.id % 6 == 0:
        product.thumbnail_url = big_product_image2
        product.save()

for product in products:
    if product.id % 4 == 1:
        product.content_image_url = content_image1
        product.save()
    if product.id % 4 == 2:
        product.content_image_url = content_image2
        product.save()
    if product.id % 4 == 3:
        product.content_image_url = content_image3
        product.save()
    if product.id % 4 == 0:
        product.content_image_url = content_image4
        product.save()

for num in range(1, len(products)+1):
    products = ProductSelection.objects.filter(product_id=num).order_by('size')
    if len(products) == 1:
        a = ProductSelection.objects.get(product_id=num)
        if num % 6 == 1:
            a.image_url = big_product_image1
            a.save()
        if num % 6 == 2:
            a.image_url = big_product_image6
            a.save()
        if num % 6 == 3:
            a.image_url = big_product_image3
            a.save()
        if num % 6 == 4:
            a.image_url = big_product_image4
            a.save()
        if num % 6 == 5:
            a.image_url = big_product_image5
            a.save()
        if num % 6 == 0:
            a.image_url = big_product_image2
            a.save()
    if len(products) == 2:
        if num % 6 == 1:
            a = products[0]
            a.image_url = small_product_image1
            a.save()
            b = products[1]
            b.image_url = big_product_image1
            b.save()
        if num % 6 == 2:
            a = products[0]
            a.image_url = small_product_image6
            a.save()
            b = products[1]
            b.image_url = big_product_image6
            b.save()
        if num % 6 == 3:
            a = products[0]
            a.image_url = small_product_image3
            a.save()
            b = products[1]
            b.image_url = big_product_image3
            b.save()
        if num % 6 == 4:
            a = products[0]
            a.image_url = small_product_image4
            a.save()
            b = products[1]
            b.image_url = big_product_image4
            b.save()
        if num % 6 == 5:
            a = products[0]
            a.image_url = small_product_image5
            a.save()
            b = products[1]
            b.image_url = big_product_image5
            b.save()
        if num % 6 == 0:
            a = products[0]
            a.image_url = small_product_image2
            a.save()
            b = products[1]
            b.image_url = big_product_image2
            b.save()

# CSV_PATH_PRODUCTS = './wesop.csv'

# with open(CSV_PATH_PRODUCTS) as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
        # Menu.objects.create(name=row[0])
        
        # menu_name = row[0]
        # menu_id = Menu.objects.get(name=row[0]).id

        # Category.objects.create(menu_id=menu_id, name=row[1], description_title=row[2], description=row[3])

        # FeatureCategory.objects.create(name=row[0])

        # feature_category_id=FeatureCategory.objects.get(name=row[0]).id
        # Feature.objects.create(feature_category_id=feature_category_id, name=row[1])

        # Ingredient.objects.create(name=row[0])

        # category_name = row[0]
        # category_id = Category.objects.get(name=category_name).id

        # Product.objects.create(category_id=category_id, name=row[1], summary=row[2], thumbnail_url=row[3], description=row[4], content=row[5], content_image_url=row[6], count=row[7])

        # product_name = row[0]
        # product_id = Product.objects.get(name=product_name).id

        # ProductSelection.objects.create(product_id=product_id, size=row[1], price=row[2], image_url=row[3])

        # product_name = row[0]
        # product = Product.objects.get(name=product_name)
        # feature_name = row[1]
        # feature_id = Feature.objects.get(name=feature_name).id

        # product.feature.add(feature_id)

        # product_name = row[0]
        # product = Product.objects.get(name=product_name)
        # ingredient_name = row[1]
        # ingredient_id = Ingredient.objects.get(name=ingredient_name).id

        # product.ingredient.add(ingredient_id)

        # SkinType.objects.create(name=row[0])

        # PaymentMethod.objects.create(name=row[0])

        # OrderStatus.objects.create(name=row[0])
