from rest_framework import serializers

from .models import ProductApi


class ProductApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductApi
        fields = '__all__'
