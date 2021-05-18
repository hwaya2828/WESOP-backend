import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wesop.settings") 
django.setup()
#장고 외부 파일이기 때문에, 장고 내 나의 프로젝트에 연결

from products.models import *

CSV_PATH_PRODUCTS = './products.csv' # update py의 경로를 변수화

with open(CSV_PATH_PRODUCTS) as products:
    data_reader = csv.reader(products)
    for row in data_reader:
        print(row)
