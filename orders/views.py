import json, re, bcrypt, jwt

from datetime               import datetime, timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View

from my_settings            import SECRET
from orders.models          import WishList, OrderList, Order, PaymentMethod, OrderStatus
from products.models        import Product, ProductSelection
from users.models           import User
from users.utils            import Authorization_decorator

class CartView(View):
    @Authorization_decorator
    def post(self, request):
        data      = json.loads(request.body)

        selection = ProductSelection.objects.get(product_id = data['product_id'], size = data['size'])
        status_id = OrderStatus.objects.get(name='주문 전').id
        user_id   = request.user.id
        
        order, created = Order.objects.get_or_create(status_id=status_id, user_id=user_id, defaults={
                'user_id' : user_id,
                'status_id':status_id, 
                'address' : '',
                'memo': '',
                'total_price' : '0',
                'free_delivery' : False
        })

        if OrderList.objects.filter(product_selection_id=selection.id, order_id=order.id).exists(): 
            cartlist = OrderList.objects.get(product_selection_id=selection.id, order_id=order.id)
            cartlist.quantity += 1
            cartlist.save()
        else:
            OrderList.objects.create(
            order_id = Order.objects.get(status_id=status_id, user_id=user_id).id,
            product_selection_id= selection.id,
            quantity = 1
        )        

        return JsonResponse({'MESSAGE':'Product add in cart.'}, status=200)

    @Authorization_decorator
    def delete(self, request):
        try:
            data      = json.loads(request.body)
            
            user_id    = request.user.id
            status_id  = OrderStatus.objects.get(name='주문 전').id
            order_id   = Order.objects.get(status_id = status_id, user_id = user_id)
            selection  = ProductSelection.objects.get(product_id = data['product_id'], size=data['size'])
            
            OrderList.objects.get(product_selection_id = selection.id, order_id=order_id).delete() 
            
            return JsonResponse({'MESSAGE':'Product deleted from cart.'}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)

        except OrderList.DoesNotExist:
            return JsonResponse({'MESSAGE':'already not exist in cart'}, status=400)
        
    @Authorization_decorator
    def patch(self, request):
        try:
            data              = json.loads(request.body)

            user_id           = request.user.id
            status_id         = OrderStatus.objects.get(name='주문 전').id
            order_id          = Order.objects.get(status_id = status_id, user_id = user_id)
            selection         = ProductSelection.objects.get(product_id = data['product_id'], size=data['size'])
            cartlist          = OrderList.objects.get(product_selection_id = selection.id, order_id=order_id) 
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
            user_id     = request.user.id
            status_id   = OrderStatus.objects.get(name='주문 전').id
            order_id    = Order.objects.get(status_id = status_id, user_id = user_id)
            cartlists   = OrderList.objects.filter(order_id = order_id)
            result      = []
            
            for cartlist in cartlists:
                selection_id = cartlist.product_selection_id
                product_id   = ProductSelection.objects.get(id=selection_id).product_id

                cart_dict = {
                    'name'      :Product.objects.get(id=product_id).name,
                    'size'      :ProductSelection.objects.get(id=selection_id).size,
                    'quantity'  :cartlist.quantity,
                    'price'     :ProductSelection.objects.get(id=selection_id).price,
                    'added_at'  :Order.objects.get(status_id=status_id, user_id=user_id).purchased_at,
                    'product_id':product_id
                }
                result.append(cart_dict)

            return JsonResponse({'result':result}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)
        except Order.DoesNotExist:
            return JsonResponse({'MESSAGE':'nothing in cart'}, status=400)


class OrderCheckView(View):
    @Authorization_decorator
    def get(self, request):
        try:
            user           = request.user
            status_id      = OrderStatus.objects.get(name='주문 전').id
            status_id_done = OrderStatus.objects.get(name='주문 후').id
            
            if (not Order.objects.filter(status_id=status_id, user_id=user.id)):
                raise Exception

            order          = Order.objects.get(status_id=status_id, user_id=user.id) 
            cartlists      = OrderList.objects.filter(order_id=order.id)

            result=[]

            total_price = 0

            for cartlist in cartlists:
                selection_id = cartlist.product_selection_id
                select       = ProductSelection.objects.get(id=selection_id)
                total        = select.price * cartlist.quantity
                total_price  = total_price + total

            Order.objects.filter(status_id=status_id, user_id=user.id).update(
                    status_id    = status_id_done, 
                    address      = user.address,
                    memo         = '',
                    total_price  = total_price if (total_price >= 50000) else (total+3000), 
                    free_delivery= True if (total_price >= 50000) else False 
                )
            
            # OrderList.objects.filter(order_id=order.id).delete()

            return JsonResponse({'MESSAGE':"SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)

        except Exception as e:
            return JsonResponse({'MESSAGE':'nothing in cart'}, status=400)

class OrderGetView(View):
    @Authorization_decorator
    def get(self, request):
        try:
            user        = request.user
            status_id_done = OrderStatus.objects.get(name='주문 후').id

            if (not Order.objects.filter(status_id=status_id_done, user_id=user.id)):
                raise Exception

            orders = Order.objects.filter(status_id=status_id_done, user_id=user.id) 
            result = []

            for order in orders:
                products = list(OrderList.objects.filter(order_id=order.id))

                for product in products:
                    selection_id = product.product_selection_id
                    select    = ProductSelection.objects.get(id=selection_id)

                    order_dict = {
                            'name'        : Product.objects.get(id=select.product_id).name,
                            'quantity'    : product.quantity ,
                            'total_price' : select.price * product.quantity,
                            'purchased_at': order.purchased_at,
                            'address'     : order.address
                        } 
                    result.append(order_dict)

            return JsonResponse({'result':result}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)

        except Exception as e:
            return JsonResponse({'MESSAGE':'NO ORDER HISTORY'}, status=400)
