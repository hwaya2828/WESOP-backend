import json
import datetime               

from django.http   import JsonResponse
from django.views  import View

from orders.models import WishList, OrderList, Order, PaymentMethod
from users.models  import Address
from users.utils   import login_confirm

class WishListVew(View):
    @login_confirm
    def get(self, request):
        user     = request.user
        products = [wishlist.product for wishlist in WishList.objects.filter(user=user)]

        result = [
                    {
                        'product_id'            : product.id,
                        'product_name'          : product.name,
                        'product_thumbnail_url' : product.thumbnail_url,
                        'product_selections'    : [
                                {
                                    'size'  : product_selection.size,
                                    'price' : product_selection.price
                                } for product_selection in product.productselection_set.all() 
                        ]
                    } for product in products 
        ]

        return JsonResponse({'result': result}, status=200)

    @login_confirm
    def post(self, request):
        user = request.user
        data = json.loads(request.body)

        if WishList.objects.filter(user=user, product_id=data['product_id']).exists():
            return JsonResponse({'result': 'ALREADY_EXIT_ERROR'}, status=400)

        WishList.objects.create(user=user, product_id=data['product_id'])

        return JsonResponse({'result': 'SUCCESS'}, status=201)

class ModifyWishListVew(View):
    @login_confirm
    def delete(self, request, product_id):
        user  = request.user

        if not WishList.objects.filter(user=user, product_id=product_id).exists():
            return JsonResponse({'message': 'DOES_NOT_EXIST_ERROR'}, status=400)

        WishList.objects.filter(user=user, product_id=product_id).delete()
            
        return JsonResponse({'result': 'SUCCESS'}, status=204)

class CartListView(View):
    @login_confirm
    def get(self, request):
        user  = request.user
        order = Order.objects.get(user=user, status__name='장바구니')

        result = {
                    'order_id' : order.id,
                    'products' : [
                                    {
                                        'product_id'       : order_list.product_selection.product.id,
                                        'product_name'     : order_list.product_selection.product.name,
                                        'product_size'     : order_list.product_selection.size,
                                        'product_price'    : order_list.product_selection.price,
                                        'product_quantity' : order_list.quantity
                                    } for order_list in OrderList.objects.filter(order=order)
                    ]
        }

        return JsonResponse({'result': result}, status=200)

    @login_confirm
    def post(self, request):
        user = request.user
        data = json.loads(request.body)

        if not Order.objects.filter(user=user, status__name='장바구니').exists():
            order = Order.objects.create(user=user, status_id=1)
            OrderList.objects.create(order=order, product_selection_id=data['product_selection_id'], quantity=1)
        else:
            order = Order.objects.get(user=user, status__name='장바구니')
            if OrderList.objects.filter(order=order, product_selection_id=data['product_selection_id']).exists():
                orderlist = OrderList.objects.get(order=order, product_selection_id=data['product_selection_id'])
                orderlist.quantity += 1
                orderlist.save()
            else:
                OrderList.objects.create(order=order, product_selection_id=data['product_selection_id'], quantity=1)

        return JsonResponse({'result': 'SUCCESS'}, status=201)
    
class ModifyCartListView(View):
    @login_confirm
    def patch(self, request, product_selection_id):
        user  = request.user
        data  = json.loads(request.body)
        order = Order.objects.get(user=user, status__name='장바구니')

        if not OrderList.objects.filter(order=order, product_selection=product_selection_id).exists():
            return JsonResponse({'message': 'DOES_NOT_EXIST_ERROR'}, status=400)
            
        orderlist          = OrderList.objects.get(order=order, product_selection=product_selection_id)
        orderlist.quantity = data['quantity']
        orderlist.save()

        return JsonResponse({'result': 'SUCCESS'}, status=200)

    @login_confirm
    def delete(self, request, product_selection_id):
        user  = request.user
        order = Order.objects.get(user=user, status__name='장바구니')

        if not OrderList.objects.filter(order=order, product_selection=product_selection_id).exists():
            return JsonResponse({'message': 'DOES_NOT_EXIST_ERROR'}, status=400)

        OrderList.objects.get(order=order, product_selection=product_selection_id).delete()
            
        return JsonResponse({'result': 'SUCCESS'}, status=204)

class OrderView(View):
    @login_confirm
    def get(self, request):
        user   = request.user
        orders = Order.objects.prefetch_related('orderlist_set').filter(user=user, status__name='구매완료')

        result = [
                    {
                        'address'        : order.address.address if order.address else None,
                        'memo'           : order.memo if order.memo else None,
                        'payment_method' : order.payment_method.name if order.payment_method else None,
                        'purchased_at'   : order.purchased_at,
                        'total_price'    : order.total_price,
                        'free_delivery'  : order.free_delivery,
                        'products'       : [
                                                {
                                                    'product_id'       : order_list.product_selection.product.name,
                                                    'product_name'     : order_list.product_selection.product.name,
                                                    'product_size'     : order_list.product_selection.size,
                                                    'product_price'    : order_list.product_selection.price,
                                                    'product_quantity' : order_list.quantity
                                                } for order_list in order.orderlist_set.all()
                                            ]
                    } for order in orders
        ]

        return JsonResponse({'result': result}, status=200)

    @login_confirm
    def post(self, request):
        try:
            user = request.user
            data = json.loads(request.body)

            if not Order.objects.prefetch_related('orderlist_set').filter(id=data['order_id']).exists():
                return JsonResponse({'message': 'DOES_NOT_EXIST_ERROR'}, status=400)
            
            if Order.objects.get(id=data['order_id']).status_id == 2:
                return JsonResponse({'message': 'ALREADY_PAYED_ERROR'}, status=400)

            order           = Order.objects.prefetch_related('orderlist_set').get(id=data['order_id'])
            address, create = Address.objects.get_or_create(user=user, address=data['address'])
            payment_method  = PaymentMethod.objects.get(id=data['payment_method_id'])
            total_price     = sum([order_list.product_selection.price * order_list.quantity for order_list in order.orderlist_set.all()])

            FREE_DELIVERY = 30000

            order.status_id      = 2
            order.address        = address
            order.memo           = data.get('memo', None)
            order.payment_method = payment_method if payment_method else None
            order.total_price    = total_price
            order.free_delivery  = True if total_price > FREE_DELIVERY else False
            order.purchased_at   = datetime.datetime.now()
            order.save()

            return JsonResponse({'result': 'SUCCESS'}, status=200)

        except KeyError: 
            return JsonResponse({'message':'KEY_ERROR'}, status=400)