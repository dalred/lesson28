from django_filters.filterset import FilterSet
from ads.models import Ad
import django_filters

# TODO как указывать например price&price непонятно так как одинаковые имена указывать нельзя
# The above would generate ‘price__lt’, ‘price__gt’, ‘price’, name__icontains, category__id filters.
from users.models import User


class ADFilter(FilterSet):
    class Meta:
        model = Ad
        fields = {
            'price': ['exact', 'gt', 'lt'],
            'name': ['icontains'],
            'category__id': ['exact']
        }

class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'ad__is_published': ['exact']
        }

#TODO можно ли сделать было по другому?
#https://django-filter.readthedocs.io/en/stable/guide/usage.html?highlight=super().qs#filtering-the-primary-qs
class ArticleFilter(FilterSet):

    class Meta:
        model = Ad
        fields = ['author']

    @property
    def qs(self):
        #parent queryset
        parent = super().qs
        author = getattr(self.request, 'user', None)
        return parent.filter(author=author)
