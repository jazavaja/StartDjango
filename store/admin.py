from django.contrib import admin

from store.models import Category, Product

# Register your models here.


# Register model in admin

# Method 1

# admin.site.register(Category)
# admin.site.register(Product)


# Method 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 4
    list_display = ('name', 'key')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ('name', 'price', 'category')
