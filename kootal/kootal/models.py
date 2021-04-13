# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BankDetails(models.Model):
    account_holder_name = models.CharField(max_length=255, null=False )
    account_number = models.CharField(max_length=255, null=False )
    bank_name = models.CharField(max_length=255, null=False )
    ifsc_code = models.CharField(max_length=255, null=False )
    branch = models.CharField(max_length=255, null=False )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_details'

    def __str__(self):
        return self.account_holder_name + " ----> " + self.bank_name + " ----> " + self.account_number

class Customer(models.Model):
    customer = models.CharField(max_length=255, null=False )
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=255, null=False , blank=True)
    bank_details = models.ForeignKey(BankDetails, models.DO_NOTHING, db_column='bank_details', blank=True, null=True)
    phone_number = models.CharField(max_length=255, null=False , blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.customer


class OrdersDetailsManager(models.Manager):

    def create(self, **obj_data):
        obj_data['total'] = obj_data['quantity'] * obj_data['price']
        return obj_data


class OrderDetails(models.Model):
    orders = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=65535, decimal_places=2)
    total = models.DecimalField(max_digits=65535, decimal_places=2 )
    # gst = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True) # gst number can be taken from customer
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_details'

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price
        super(OrderDetails, self).save(*args, **kwargs)



from enum import Enum
class OrderTypes(Enum):
    purchase = "purchase"
    sell = "sell"


class Orders(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    order_type = models.CharField(max_length=255, choices=[('purchase', 'purchase'), ('sell', 'sell')]
                                  ,blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return self.customer.customer + " ----> " + self.order_type

class Owner(models.Model):
    active = models.BooleanField(blank=True, null=True)
    owner_name = models.CharField(max_length=255, null=False , blank=True)
    gst_number = models.CharField(max_length=255, null=False , blank=True)
    address = models.TextField(blank=True, null=True)
    bank_details = models.ForeignKey(BankDetails, models.DO_NOTHING, db_column='bank_details', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    phone_number = models.CharField(max_length=255, null=False , blank=True)

    class Meta:
        managed = False
        db_table = 'owner'


class Product(models.Model):
    product_name = models.CharField(max_length=255, null=False )
    hscn_number = models.CharField(max_length=255, null=False , blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self):
        return self.product_name

class Transaction(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='order', blank=True, null=True)
    bill_number = models.CharField(max_length=255, null=False , blank=True)
    amount_received = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_sent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction'

