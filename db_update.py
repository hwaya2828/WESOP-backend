import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wesop.settings") 
django.setup()
#장고 외부 파일이기 때문에, 장고 내 나의 프로젝트에 연결

from products.models import *

CSV_PATH_PRODUCTS= './CSV/menu.csv'
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        menu_name = row[0]
        update,create = Menu.objects.update_or_create(name= menu_name)
        update.save()

CSV_PATH_PRODUCTS= './CSV/menu.csv'
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        menu_name = row[0]
        menu_id = Menu.objects.get(name= menu_name).id
        category_name = row[1] 
        description_title= row[2] 
        # if row[2] else ''
        description= row[3] 
        # if row[3] else ''

        update,create=Category.objects.update_or_create(
            name=category_name,
            description_title=description_title,
            description=description,
            menu_id =  menu_id
            )
        update.save()

CSV_PATH_PRODUCTS= './CSV/category.csv'
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        category = row[0]
        category_id = Category.objects.get(name=category).id
        name = row[1]
        summary = row[2]
        thumbnail_url = row[3]
        description = row[4]
        content = row[5]
        content_image_url= row[6]
        count = row[7]

        update, create= Product.objects.update_or_create(
            name = name,
            summary=summary,
            thumbnail_url = thumbnail_url,
            description = description,
            content = content,
            content_image_url =  content_image_url,
            count = count,
            category_id =category_id
        )
        update.save()

CSV_PATH_PRODUCTS= './CSV/product_selection.csv'
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        product = row[0]
        product_id = Product.objects.get(name=product).id
        size = row[1]
        price = row[2]
        image_url = row[3]

        update, create= ProductSelection.objects.update_or_create(
            size =  size,
            price = price,
            image_url = image_url,
            product_id = product_id
        )
        update.save()