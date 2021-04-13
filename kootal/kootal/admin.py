from django.contrib import admin
from .models import *
from django.db.models import Sum

class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ('account_holder_name', 'account_number', 'bank_name', 'ifsc_code', 'branch')
    list_filter = ("update_date",)

    class Meta:
        exclude = ['create_date', 'update_date']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer", "address", "gst_number", "bank_details", "phone_number")
    search_fields = ("customer__startswith",)
    list_filter = ("update_date",)

    class Meta:
        exclude = ['create_date', 'update_date']

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'gst_number', 'address', 'bank_details', 'phone_number')
    list_filter = ("update_date",)

    class Meta:
        exclude = ['create_date', 'update_date']

class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "hscn_number")
    search_fields = ("product_name__startswith",)
    list_filter = ("update_date",)

    class Meta:
        exclude = ['create_date', 'update_date']

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    readonly_fields = ('total', )

class OrderDetailsAdmin(admin.ModelAdmin):
    inlines = (OrderDetailsInline, )
    list_display = ('customer', 'order_type', 'total_order_amount', 'update_date')
    # list_display = ('get_customer', 'get_order_type', 'get_update_date')
    # list_display_links = ('get_customer', )

    list_filter = ("update_date",)

    def get_customer(self, obj):
        return obj.Orders.customer

    def get_order_type(self, obj):
        return obj.Orders.order_type

    def get_update_date(self, obj):
        return obj.Orders.update_time

    def total_order_amount(self, obj):
        return OrderDetails.objects.filter(orders = obj.id).aggregate(Sum('total')).get('total__sum')


admin.site.register(BankDetails, BankDetailsAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Orders, OrderDetailsAdmin)