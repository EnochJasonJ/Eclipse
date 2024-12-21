from rest_framework import serializers
from .models import UserModel, ProductModel, OrderModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    class Meta:
        model = OrderModel
        fields = ['user','product','quantity','total_price']
        read_only_fields = ['total_price']


    def validate(self,attrs):
        product = attrs.get('product')
        quantity = attrs.get('quantity')

        if product.stocks < quantity:
            raise serializers.ValidationError("Not enough stock available.")
            
        attrs['total_price'] = product.price * quantity
        return attrs
        

    def create(self, validate_data):
        product = validate_data['product']
        quantity = validate_data['quantity']

        product.stocks -= quantity
        product.save()

        order = OrderModel.objects.create(**validate_data)
        return order



