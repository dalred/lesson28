from django_filters.filterset import FilterSet
from ads.models import Ad

# TODO как указывать например price&price непонятно так как одинаковые имена указывать нельзя
# The above would generate ‘price__lt’, ‘price__gt’, ‘price’, name__icontains, category__id filters.
class ADFilter(FilterSet):
    class Meta:
        model = Ad
        fields = {
            'price': ['exact', 'gt', 'lt'],
            'name': ['icontains'],
            'category__id': ['exact']
        }
