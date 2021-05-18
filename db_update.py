import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wesop.settings") 
django.setup()
#장고 외부 파일이기 때문에, 장고 내 나의 프로젝트에 연결

from products.models import *

# CSV_PATH_PRODUCTS = './products.csv' # update py의 경로를 변수화
# def insert_products(): #data crud 시 insert_products()라고 선언하기만 하면 된다
#     with open(CSV_PATH_PRODUCTS) as products:
#     data_reader = csv.reader(products)
#     next(data_reader, None) #upload 시 1열의 컬럼 제목 제외
#     for row in data_reader:
#         print(row)
#         print(row[0])
#         if row[0] !='':
#             print(row[0])
#             menu_name = row[0] # menu row
#             Menu.objects.create(name = menu_name)

#         category_name = row[1] #category row
#         print(menu_name, category_name)
#         menu_id= Menu.objects.get(name=menu_name).id #foreign key 연결관련

#         Category.objects.create(name=category_name, menu_id=menu_id) #category 입력
#         Category_id = Category.objects.get(name=category_name).id

#         drinks = row[2].split('.') #drink row split하여 변수에 담음
#         for drink in drinks:
#             if drinks:
#                 Drink.objects.create(name=drink, menu_id=menu_id, category_id=Category_id) # drink 입력
#         update.save()

CSV_PATH_PRODUCTS= './CSV/menu.csv'
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        menu_name = row[0]
        # product_name = row[1]
        # cost = row[2]
        # description_iamge_url = row[3]
        # category_object=Category.objects.get(name=category_name)
        # update, create = Product.objects.update_or_create(
        #     category=category_object,
        #     name=product_name,
        #     cost=float(cost),
        #     description_iamge_url=description_iamge_url
        #     )
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