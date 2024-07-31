from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    category = models.CharField(
        verbose_name= "カテゴリー",
        max_length= 20,
    )
    def __str__(self):
        return self.category

class Menu(models.Model):
    title = models.CharField(
        verbose_name="商品名",
        max_length = 20,
    )
    image = models.ImageField(
        verbose_name='商品画像',
        upload_to="image",
        null=True,
    )
    body = models.TextField(
        verbose_name='商品説明',
    )

    price = models.IntegerField(
        verbose_name='価格',
    )
    
    category = models.ForeignKey(
        Category,
        verbose_name= 'カテゴリー',
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.title