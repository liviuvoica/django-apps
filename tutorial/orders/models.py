from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.IntegerField()
    order_value = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)