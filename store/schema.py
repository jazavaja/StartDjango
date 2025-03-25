import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload
from .models import Product, Category


# تعریف نوع داده برای Category
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "key")


# تعریف نوع داده برای Product
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "category", "price", "picture")


# تعریف Query
class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product_by_id = graphene.Field(ProductType, id=graphene.ID(required=True))
    all_categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID(required=True))

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_product_by_id(root, info, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_category_by_id(root, info, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None


# تعریف Mutation برای ایجاد محصول
class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        category_id = graphene.ID(required=True)
        price = graphene.Decimal(required=True)
        picture = Upload(required=False)  # برای آپلود فایل

    product = graphene.Field(ProductType)

    def mutate(root, info, name, category_id, price, picture=None):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise Exception("Category with the given ID does not exist.")

        product = Product(name=name, category=category, price=price, picture=picture)
        product.save()
        return CreateProduct(product=product)

# تعریف Mutation برای ایجاد دسته‌بندی
class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(root, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    create_category = CreateCategory.Field()


# تعریف Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
