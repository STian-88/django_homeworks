from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']

class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['stock_id', 'product', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['address', 'positions']


    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            position.update(dict(stock_id=stock.id))
            StockProduct.objects.create(**position)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            product_id = Product.objects.get(title=position['product']).id
            position.update(dict(stock_id=stock.id, product_id=product_id))
            ids = set([item.product_id for item in StockProduct.objects.filter(stock_id=stock.id)])
            if product_id in ids:
                item = StockProduct.objects.get(product_id=position['product_id'], stock_id=position['stock_id'])
                item.quantity = position.get('quantity', item.quantity)
                item.price = position.get('price', item.price)
                item.save()
            else:
                StockProduct.objects.create(**position)
        return stock
