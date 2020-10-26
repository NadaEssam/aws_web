from django.db import models

# Create your models here.
class Product(models.Model):
        name = models.CharField(max_length=200,null=True)
        description = models.TextField(null=True)
        manufacturer_name = models.CharField(max_length=200, null=True)
        inventory_count = models.IntegerField(null=True)

        def __str__(self):
            return self.name


class User(models.Model):
        name = models.CharField(max_length=200,null=True)
        password = models.CharField(max_length=200,null=True)
        Preference = models.CharField(max_length=20, null=True)

        def __str__(self):
            return self.name


class Product_bought(models.Model):
        user_id = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
        product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
        user_name = models.CharField(max_length=200,null=True)
        product_name = models.CharField(max_length=200,null=True)
        quantity = models.IntegerField(null=True)
        date_of_purchase = models.DateField(null=True)
