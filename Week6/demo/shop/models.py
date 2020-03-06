from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)

    def to_json(self):
        return {
            'id': self.id,
            'category_name': self.category_name,
            'rating': self.rating,
        }


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)

    def to_json(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'price': self.price,
            'category': self.category,
            'created_by': self.created_by
        }
