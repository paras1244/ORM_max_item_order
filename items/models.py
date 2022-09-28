from django.db import models

# Create your models here.


class Order(models.Model):
    cus_name = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.cus_name)

class Items(models.Model):
    product_name = models.CharField(max_length=25)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
    
    def __str__(self):
        return self.product_name

        # return '%s: %d' % (self.product_name, self.quantity)
        # return (self.product_name, str(self.quantity))
