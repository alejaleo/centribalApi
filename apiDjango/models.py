from django.db import models

class Article(models.Model):
    id=models.AutoField(primary_key=True)
    reference=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    priceWithOutTaxes=models.DecimalField(max_digits=10,decimal_places=2)
    taxes=models.DecimalField(max_digits=10,decimal_places=2)
    createdAtArticle=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    id=models.AutoField(primary_key=True)
    listArticles=models.JSONField()
    priceTotalWithOutTaxes=models.DecimalField(max_digits=10, decimal_places=2)
    priceTotalWithTaxes=models.DecimalField(max_digits=10,decimal_places=2)
    createdAtOrders=models.DateTimeField(auto_now_add=True)