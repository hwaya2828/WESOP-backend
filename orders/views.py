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
        


class OrderCheckView(View):
    @Authorization_decorator
    def get(self, request):
        try:
            user           = request.user
            status_id      = OrderStatus.objects.get(name='주문 전').id
            status_id_done = OrderStatus.objects.get(name='주문 후').id
            
            # (not OrderList.objects.all()) and
            if (not Order.objects.filter(status_id=status_id)):
                raise Exception
                
            order          = Order.objects.filter(status_id=status_id) 
            cartlists      = OrderList.objects.all() 

            result=[]

            for cartlist in cartlists:
                selection_id = cartlist.product_selection_id
                select       = ProductSelection.objects.get(id=selection_id)
                total        = select.price * cartlist.quantity
                # Order.objects.filter(status_id=status_id)
                order.update(
                        status_id    = status_id_done, 
                        address      = user.address,
                        memo         = '',
                        total_price  = total if (total >= 50000) else (total+3000), 
                        free_delivery= True if (total >= 50000) else False 
                    )
            
                order_dict = {
                    'name': Product.objects.get(id=select.product_id).name,
                    'quantity': cartlist.quantity ,
                    'total_price': Order.objects.get(id=cartlist.order_id).total_price,
                    'purchased_at': Order.objects.get(id=cartlist.order_id).purchased_at,
                    'address': User.objects.get(id=user.id).address
                } # 주문내용 어떤거 return?, address 없는 경우 입력하세요도 필요?
                result.append(order_dict)

            OrderList.objects.all().delete()

            return JsonResponse({'result':result}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)

        # except Order.DoesNotExist:
        #     return JsonResponse({'MESSAGE':'nothing in cart'}, status=400)

        except Exception as e:
            return JsonResponse({'MESSAGE':'nothing in cart'}, status=400)