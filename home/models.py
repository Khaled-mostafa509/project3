from django.db import models
# from authentications.models import User

# Create your models here.





class Products(models.Model):
    id=models.AutoField(primary_key=True,name="product_id")
    Name=models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    Category=models.CharField(max_length=25)
    price = models.CharField(max_length=10,null= True)
    Production_country = models.CharField( max_length=50)
    image = models.ImageField( null= True)

    
    
    
    
    def __str__(self):
        return self.Name

class Category(models.Model):
    id=models.AutoField(primary_key=True,name="category_id")
    Name = models.CharField(max_length=25)
    category_products = models.ManyToManyField("Products",related_name="categories")
    
    def __str__(self):
        return self.Name 
   
class Recommended(models.Model):
    id=models.AutoField(primary_key=True,name="recommend_id")
    product_name = models.ForeignKey("Products", on_delete=models.CASCADE) 
    recomended_devices = models.ManyToManyField("Products",related_name="aa") 
    
    def __str__(self):
        return self.recomended_devices
       

class OrderItem(models.Model):
    id=models.AutoField(primary_key=True,name="orderitem_id")
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.quantity} of {self.item.Name}"
    
class Order(models.Model):
    id=models.AutoField(primary_key=True,name="order_id")
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
