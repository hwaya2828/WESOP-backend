
import json, re, bcrypt, jwt

from datetime     import datetime, timedelta

from django.http  import JsonResponse
from django.views import View

from orders.models  import WishList, OrderList, Order, PaymentMethod, OrderStatus
from products.models import Product, ProductSelection
from users.models   import User
from my_settings    import SECRET

from users.utils  import decorator

class CartAddView(View):
    @decorator
    def Post(self, request):
        data    = json.loads(request.body)

        product = ProductSelection.objects.filter(id = data['product_id'])
        size    = product.get(size = data['size'])
        user_id = request.user.id

        if not Order.objects.get(status_id = 2).exist():
            Order.objects.create(
                user_id = user_id,
                status_id=2, #status table에 yes 는 id 1 , no는 id 2로 설정 예정
                address='',
                memo='',
                total_price= 0,
                free_delivery=False
            )

        orders=Order.object.get(status_id = 2)

        OrderList.objects.create(
            order_id = orders.id,
            product_selection_id= size.id,
            quantity = 1
        )        
        
        return JsonResponse({'MESSAGE':'Product add in cart.'}, status=200)

class CartDeleteView(View):
    @decorator
    def Post(self, request):
        try:
            data    = json.loads(request.body)
            selection_id = ProductSelection.objects.filter(product_id = data['product_id'], size=data['size']).id
            OrderList.objects.get(production_selection_id = selection_id).delete() #에러

            return JsonResponse({'MESSAGE':'Product deleted from cart.'}, status=200)
        except :
            return JsonResponse({'MESSAGE':'noting in cart'}, status=200)

class CartQuantityView(View):
    @decorator
    def Post(self, request):
        try:
            data    = json.loads(request.body)
            selection_id = ProductSelection.objects.filter(product_id = data['product_id'], size=data['size']).id
            cartlist    = OrderList.objects.get(production_selection_id = selection_id) #에러
            cartlist.quantity = data['quantity']
            return JsonResponse({'MESSAGE':'Product quantity in cart updated.'}, status=200)
        
        except :
            return JsonResponse({'MESSAGE':'noting in cart'}, status=200)

class CartCheckView(View):
    @decorator
    def get(self, request):
        try:
            cartlists   = OrderList.objects.all() #에러 except
            result = []
            for cartlist in cartlists:
                selection_id = cartlist.product_selection_id
                product_id   = ProductSelection.objects.get(id=selection_id).product_id
                status_id    = cartlist.status_id
                cart_dict = {
                    'name':Product.object.get(id=product_id).name,
                    'size':ProductSelection.objects.get(id=selection_id).size,
                    'quantity': cartlist.quantity,
                    'price' : ProductSelection.objects.get(id=selection_id).price,
                    'added_at' : Order.objects.get(status_id=status_id).purchased_at
                }
                result.append(cart_dict)

            return JsonResponse({'result':result}, status=200)

        except :
            return JsonResponse({'MESSAGE':'noting in cart'}, status=200)

class OrderCheckView(View):
    @decorator
    def Post(self, request):
        try:
            data    = json.loads(request.body)

            user = request.user
            order_id= Order.objects.get(status_id=2).id #에러 except
            cartlists = OrderList.objects.all() #에러 except 

            for cartlist in cartlists:
                selection_id = cartlist.product_selection_id
                select        = ProductSelection.objects.filter(id=selection_id)
                total        = select.price * cartlist.quantity

                Order.objects.filter(status_id=2).update(
                        status_id=1, #status table에 yes 는 id 1 , no는 id 2로 설정 예정
                        address=user.address,
                        memo='',
                        total_price=total if total >= 50000 else total+3000,
                        free_delivery=True if total >= 50000 else False
                    )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except:
                return JsonResponse({'MESSAGE':'noting in cart'}, status=200)