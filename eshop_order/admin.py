from django.contrib import admin
from .models import Order, OrderDetail


# Register your models here.

class AdminOrder(admin.ModelAdmin):
    list_display = ['owner', 'is_paid']
    list_filter = ['is_paid']


admin.site.register(Order, AdminOrder)
admin.site.register(OrderDetail)
