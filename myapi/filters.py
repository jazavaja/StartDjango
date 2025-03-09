import django_filters

from myapi.models import ProductApi


class ProductApiFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='gte')
    date = django_filters.DateFilter(field_name='create_at',lookup_expr='exact')
    date_after = django_filters.DateFilter(field_name='create_at',lookup_expr='gte')
    date_before = django_filters.DateFilter(field_name='create_at',lookup_expr='lte')

    class Meta:
        model = ProductApi
        fields = ['name', 'description', 'price']
