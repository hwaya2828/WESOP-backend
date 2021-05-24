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
        user      = request.user
        selection = ProductSelection.objects.get(product_id = data['product_id'], size = data['size'])
        status    = OrderStatus.objects.get(name='주문 전')
        
        order, created = Order.objects.get_or_create(status=status, user=user, defaults={
                'user_id' : user.id,
                'status_id':status.id, 
                'address' : '',
                'memo': '',
                'total_price' : '0',
                'free_delivery' : False
        })

        cartlist = OrderList.objects.filter(product_selection=selection, order=order)
        if cartlist.exists(): 
            cartlist[0].quantity += 1
            cartlist[0].save()
        else:
            OrderList.objects.create(
            order_id            = order.id,
            product_selection_id= selection.id,
            quantity            = 1
        )        

        return JsonResponse({'MESSAGE':'Product add in cart.'}, status=200)

    @Authorization_decorator
    def delete(self, request, cart_id):
        try:
            cart = OrderList.objects.get(id=cart_id)
            
            if cart.order.status.name != '주문 전':
                return JsonResponse({'MESSAGE':'already ordered'}, status=400)
            
            cart.delete()
            return JsonResponse({'MESSAGE':'Product deleted from cart.'}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)
        except OrderList.DoesNotExist:
            return JsonResponse({'MESSAGE':'already not exist in cart'}, status=400)

    @Authorization_decorator
    def patch(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            cartlist = OrderList.objects.get(product_selection__product__id = data['product_id'], product_selection__size=data['size'],order__status__name = '주문 전', order__user = user)
            print(cartlist)
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
            user        = request.user
            carts       = OrderList.objects.filter(order__status__name = '주문 전', order__user = user)
            result      = []
            
            for cart in carts:
                cart_dict = {
                    'cart_id'   : cart.id,
                    'name'      : cart.product_selection.product.name,
                    'size'      : cart.product_selection.size,
                    'quantity'  : cart.quantity,
                    'price'     : cart.product_selection.price,
                    'added_at'  : cart.order.purchased_at,
                    'product_id': cart.product_selection.product.id
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
            user        = request.user
            status_done = OrderStatus.objects.get(name='주문 후')
            cartlists   = OrderList.objects.filter(order__status__name='주문 전', order__user=user)
            if not cartlists:
                return JsonResponse({'MESSAGE':'nothing in cart'}, status=400)
            total_price = 0
            for cartlist in cartlists:
                price        = cartlist.product_selection.price
                total        = price * cartlist.quantity
                total_price  = total_price + total
            Order.objects.filter(status__name='주문 전', user=user).update(
                    status_id    = status_done.id,
                    address      = user.address,
                    memo         = '',
                    total_price  = total_price if (total_price >= 50000) else (total+3000),
                    free_delivery= True if (total_price >= 50000) else False
                )
            return JsonResponse({'MESSAGE':"SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)
            
class OrderGetView(View):
    @Authorization_decorator
    def get(self, request):
        try:
            user           = request.user
            status_done    = OrderStatus.objects.get(name='주문 후')
            products       = OrderList.objects.filter(order__status__name='주문 후', order__user=user)
            if not products:
                return JsonResponse({'MESSAGE':'NO ORDER HISTORY'}, status=400)
            result = []
            for product in products:
                order_dict = {
                        'name'        : product.product_selection.product.name,
                        'quantity'    : product.quantity,
                        'price'       : product.product_selection.price,
                        'size'        : product.product_selection.size,
                        'date'        : product.order.purchased_at,
                        'product_id'  : product.product_selection.product.id
                    }
                result.append(order_dict)
            return JsonResponse({'result':result}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY ERROR'}, status=400)