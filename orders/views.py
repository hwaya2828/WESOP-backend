import json, re, bcrypt, jwt

from datetime     import datetime, timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View

from orders.models   import WishList, OrderList, Order, PaymentMethod, OrderStatus
from products.models import Product, ProductSelection
from users.models    import User
from my_settings     import SECRET

from users.utils     import Authorization_decorator

class CartView(View):
    @Authorization_decorator
    def post(self, request):
        data      = json.loads(request.body)
        selection = ProductSelection.objects.get(product_id = data['product_id'], size = data['size'])
        status_id = OrderStatus.objects.get(name='주문 전').id
        user_id   = request.user.id
        
        order, created = Order.objects.get_or_create(status_id=status_id, defaults={
                'user_id' : user_id,
                'status_id':status_id, 
                'address' : '',
                'memo': '',
                'total_price' : '0',
                'free_delivery' : False
        })

        if OrderList.objects.filter(product_selection_id=selection.id).exists(): 
            cartlist = OrderList.objects.get(product_selection_id=selection.id)
            cartlist.quantity += 1
            cartlist.save()
        else:
            OrderList.objects.create(
            order_id = Order.objects.get(status_id=status_id).id,
            product_selection_id= selection.id,
            quantity = 1
        )        

        # order_id = Order.objects.get(status_id=status_id).id

        # orderlist, updated = OrderList.objects.update_or_create(product_selection_id=selection.id, default={
        #             'order_id' : order_id,
        #             'product_selection_id' : selection.id,
        #             'quantity' : # 카트 내 상품이 기존재하는 경우 +1만 하려면 어떻게 표현할 수 있을까요? 
        # })
        
        return JsonResponse({'MESSAGE':'Product add in cart.'}, status=200)

    @Authorization_decorator
    def delete(self, request):
        try:
            data      = json.loads(request.body)
            selection = ProductSelection.objects.get(product_id = data['product_id'], size=data['size'])
            
            OrderList.objects.get(product_selection_id = selection.id).delete() 
            
            return JsonResponse({'MESSAGE':'Product deleted from cart.'}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)

        except OrderList.DoesNotExist:
            return JsonResponse({'MESSAGE':'already not exist in cart'}, status=400)
        
    @Authorization_decorator
    def patch(self, request):
        try:
            data              = json.loads(request.body)
            selection         = ProductSelection.objects.get(product_id = data['product_id'], size=data['size'])
            cartlist          = OrderList.objects.get(product_selection_id = selection.id) 
            cartlist.quantity = data['quantity']
            cartlist.save()
            
            return JsonResponse({'MESSAGE':'Product quantity in cart updated.'}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)

        except OrderList.DoesNotExist:
            return JsonResponse({'MESSAGE':'nothing in cart'}, status=400)

    @Authorization_decorator
    def get(self, request):
        try:
            cartlists   = OrderList.objects.all() 
            result = []
            
            for cartlist in cartlists:
                selection_id = cartlist.product_selection_id
                product_id   = ProductSelection.objects.get(id=selection_id).product_id
                order_id     = cartlist.order_id
                status_id    = Order.objects.get(id=order_id).status_id

                cart_dict = {
                    'name'    :Product.objects.get(id=product_id).name,
                    'size'    :ProductSelection.objects.get(id=selection_id).size,
                    'quantity':cartlist.quantity,
                    'price'   :ProductSelection.objects.get(id=selection_id).price,
                    'added_at':Order.objects.get(status_id=status_id).purchased_at,
                    'product_id': product_id
                }
                result.append(cart_dict)

            return JsonResponse({'result':result}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)