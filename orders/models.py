from django.db       import models

class WishList(models.Model):
    user    = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    class Meta:
        db_table = 'wish_lists'

class OrderList(models.Model):
    order             = models.ForeignKey("Order", on_delete=models.CASCADE)
    product_selection = models.ForeignKey("products.ProductSelection", on_delete=models.CASCADE)
    quantity          = models.IntegerField()

    class Meta:
        db_table = 'order_lists'

class Order(models.Model):
    user           = models.ForeignKey("users.User", on_delete=models.CASCADE)
    status         = models.ForeignKey("OrderStatus", on_delete=models.CASCADE)
    address        = models.ForeignKey("users.Address", on_delete=models.CASCADE, null=True)
    memo           = models.TextField(null=True)
    payment_method = models.ForeignKey("PaymentMethod", on_delete=models.CASCADE, null=True)
    total_price    = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    free_delivery  = models.BooleanField(default=False)
    purchased_at   = models.DateTimeField(null=True)

    class Meta:
        db_table = 'orders'

class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'payment_methods'

    
class OrderStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'order_status'