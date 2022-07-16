from dataclasses import field, fields
from django.contrib import admin

from .models import Items, Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
        list_display = [
            "id",
            "cus_name",
        ]

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product_name",
        "quantity",
    )




# Book.objects.all().aggregate(Max('price'))
# Order.objects.all().values("id","cus
# _name").annotate(count = Count("cus_name"))
# from django.db.models import Avg
