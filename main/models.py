from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    phone = models.CharField(max_length=50 , null=True)
    twitter = models.CharField(max_length=50 , null=True)
    instagram = models.CharField(max_length=50 , null=True)
    facebook = models.CharField(max_length=50 , null=True)
    image = models.ImageField( default='user.png' ,null=True , blank=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    title = models.CharField(max_length=50 , null=True)
    description = models.CharField(max_length=200 , null=True)
    rate = models.IntegerField(default=0 ,  null=True)
    price = models.FloatField(default=0 ,  null=True)
    remaining = models.IntegerField(default=1 ,  null=True)
    image = models.ImageField(default='product.jpg' , null=True , blank=True)

    def __str__(self):
        return self.title  

    @property
    def check_remaining(self):
        if self.remaining < 4 :
            return True
        else:
            return False

class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , null=True)
    complete = models.BooleanField(default = False , null=True)
    transaction_id = models.CharField(max_length=300 , null=True)
    date_ordered = models.DateField(auto_now_add=True , null=True)

    def __str__(self):
        return str(self.id)

    @property
    def totalCost(self):
        items = self.orderitem_set.all()
        return sum([item.total_price for item in items])
    
    @property
    def totalItems(self):
        items = self.orderitem_set.all()
        return sum([item.quantity for item in items])

class OrderItem(models.Model):
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null=True)
    quantity = models.IntegerField(default=1 , null=True)
    date_added = models.DateField(auto_now_add=True , null=True)

    def __str__(self):
        return self.product.title

    @property
    def total_price(self):
        return self.product.price * self.quantity 


class Shipping(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null=True)
    address = models.CharField(max_length=300 , null=True)
    city = models.CharField(max_length=200 , null=True)
    region = models.CharField(max_length=200 , null=True)
    zipcode = models.CharField(max_length=20 , null=True)
    date_added = models.DateField(auto_now_add=True , null=True)

    def __str__(self):
        return self.address





# # signal for creating customer on User creation
# def saveCustomer(sender , instance , created ,  **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
# post_save.connect(saveCustomer , sender = User)