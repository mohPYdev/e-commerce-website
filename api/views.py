from .serializers import OrderItemSerializer , ProductSerializer
from main.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def orderItemList(request):
    
    order , created = Order.objects.get_or_create(customer= request.user.customer , complete=False)
    orderitems = OrderItem.objects.filter(order=order)
    serializer = OrderItemSerializer(orderitems , many = True)
    return Response(serializer.data)

@api_view(['GET'])
def productList(request):

    products= Product.objects.filter(remaining__gt = 0)
    serializer = ProductSerializer(products , many = True)
    return Response(serializer.data)