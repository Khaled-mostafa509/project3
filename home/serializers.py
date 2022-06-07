from rest_framework import serializers
from .models import Products , Order , OrderItem ,Recommended,Category 

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    category_products =  HomeSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_id','Name','category_products']
        
class RecommendedSerializers(serializers.ModelSerializer):
    product= serializers.CharField(source='product_name.Name')
    recomended_devices =  HomeSerializers(many=True, read_only=True,)
    class Meta:
        model = Recommended
        fields = ['recommend_id','product','recomended_devices']

        
class  jsonOrderItem(serializers.ModelSerializer):
    item= serializers.CharField(source='item.Name')
    price= serializers.CharField(source='item.price')
    image= serializers.CharField(source='item.image')
    class Meta:
        model = OrderItem
        fields = "__all__"
        
class  jsonOrder(serializers.ModelSerializer):
    # items= serializers.CharField(source=f"{OrderItem.quantity} of {OrderItem.item}")
    class Meta:
        model = Order
        fields = "__all__"      
        
