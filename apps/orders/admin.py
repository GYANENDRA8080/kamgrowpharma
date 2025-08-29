from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id','customer_name','city','pincode','paid','created_at')
    list_filter = ('paid', 'created_at')
    search_fields = ('customer_name','phone','email')
