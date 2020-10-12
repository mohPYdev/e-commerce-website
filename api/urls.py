from django.urls import path 
from . import views

urlpatterns = [
    path('orderItem-list/' , views.orderItemList , name = 'orderItemList'),
    path('product-list/' , views.productList , name = 'productList'),

]