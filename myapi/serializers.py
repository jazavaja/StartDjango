from rest_framework import serializers

from .models import BookApi, AuthorApi
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


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorApi
        fields = ['id','name']


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=AuthorApi.objects.all())
    # author = serializers.StringRelatedField()
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=AuthorApi.objects.all(),
    #     view_name='author_detail',
    #     lookup_field='id'
    # )
    author = AuthorSerializer()

    class Meta:
        model = BookApi
        fields = ['id', 'author', 'title']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        print("POP: ",author_data)
        author,is_created = AuthorApi.objects.get_or_create(**author_data)
        print("author:  ",author)
        book = BookApi.objects.create(author=author,**validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author_inst = instance.author
            for key, value in author_data.items():
                setattr(author_inst, key, value)
            author_inst.save()
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
