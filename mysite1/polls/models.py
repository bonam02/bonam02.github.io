from django.db import models


class Product(models.Model):
    product = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    p_id = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)

