from rest_framework import serializers

from .models import ProductApi


class ProductApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductApi
        fields = ['name', 'id']


class ProductApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_price(self, value):
        if value < 1000:
            raise serializers.ValidationError('قیمت کالا کمتر از 1000 تومن نداریم خدا بیامرزه این قیمت هارو')
        return value

    def create(self, validated_data):
        print(validated_data)
        return {'message': 'تست کردن سریالایز بدون ذخیره کردن', 'data': validated_data}
