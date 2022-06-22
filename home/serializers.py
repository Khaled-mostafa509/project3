from rest_framework import serializers
from .models import Product , Order , OrderItem ,Recommended,Category 
from django.db import models
from authentications.models import User
class HomeSerializers(serializers.ModelSerializer):
    category= serializers.CharField()
    class Meta:
        model = Product
        fields = ['product_id','Name','description','category','price','Production_country','image']

class CategorySerializers(serializers.ModelSerializer):
    category_products =  HomeSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_id','Name','category_products']
        
class RecommendedSerializers(serializers.ModelSerializer):
    product_name= HomeSerializers(read_only=True,)
    recomended_devices =  HomeSerializers(many=True, read_only=True,)
    class Meta:
        model = Recommended
        fields = ['product_name','recomended_devices']

        
class  jsonOrderItem(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.Name')
    class Meta:
        model = OrderItem
        fields = ['item_name','quantity','price','user','item']
        
class  jsonOrder(serializers.ModelSerializer):
    # items= serializers.CharField(source=f"{OrderItem.quantity} of {OrderItem.item}")
    class Meta:
        model = Order
        fields = "__all__"      
        
