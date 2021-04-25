from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product


# Create your models here.

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده/نشده')
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount

    def tax(self):
        return self.get_total_price() * 0.09

    def get_final_amount(self):
        return self.get_total_price() + self.tax()

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    count = models.IntegerField(verbose_name='تعداد')
    price = models.IntegerField(verbose_name='قیمت محصول')

    def get_detail_sum(self):
        return self.count * self.price


    class Meta:
        verbose_name = 'جزئیات محصول'
        verbose_name_plural = 'اطلاعات جزئیات محصولات'

    def __str__(self):
        return self.product.title
