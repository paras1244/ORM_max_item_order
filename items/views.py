
# Create your views here.
from .serializers import ItemSerializer, OrderSerializer
from .models import Items, Order
from rest_framework import viewsets
from django.db.models import Count, Sum


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    # get the order list as max number of item quantity is on top
    queryset = Order.objects.all() \
        .values("id","cus_name") \
        .annotate(order_count=Sum("order__quantity")) \
        .order_by("-order_count")
    # queryset = Order.objects.all().values("id","cus_name").annotate(order_count=Sum("order__quantity")).order_by("-order_count")
    # for query in queryset:
    #     print(query)


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()