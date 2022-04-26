from ads.models import Location, Ad, Category, Author
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# Разобрал для себя
# class AuthorSerializer(serializers.ModelSerializer):
#     location_id = LocationSerializer(many=True)
#     class Meta:
#         model = Author
#         fields = ['id', 'first_name', 'last_name', 'location_id']
#
#
# class ADVLisSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()
#
#     class Meta:
#         model = Ad
#         # fields = ['id','name', 'price', 'category_id']
#         fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    # Чтобы отразить locations по name, при этому locations.name уникальное.
    # Чтобы отразить locations по id, при этому locations.id уникальное(slug_field='id').
    locations = serializers.SlugRelatedField(many=True,
                                             read_only=True,
                                             slug_field='name'
                                             )

    class Meta:
        model = Author
        fields = '__all__'


class ADVListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False,
                                            required=False,
                                            slug_field='name',
                                            queryset=Category.objects.all()
                                            )

    class Meta:
        model = Ad
        fields = ['id', 'name', 'price', 'author', 'category']


# Как обновлять с двумя ForeignKey по имени поля тоже непонятно
class ADVCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'name', 'price', 'category', 'author', 'image']


class AuthorCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True,
                                             required=False,
                                             slug_field='name',
                                             queryset=Location.objects.all()
                                             )

    class Meta:
        model = Author
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        # Словарь который передает пользователь
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        author = Author.objects.create(**validated_data)

        for location_name in self._locations:
            location, _ = Location.objects.get_or_create(name=location_name)
            author.locations.add(location)

        author.save()
        return author


class AuthorUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True,
                                             required=False,
                                             slug_field='name',
                                             queryset=Location.objects.all()
                                             )
    username = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'locations']

    # Проверка на валидность locations, что типа locations всегда есть, я бы воообще убрал,
    # может и не быть как быть?
    # def is_valid(self, raise_exception=False):
    #     # Словарь который передает пользователь
    #     self._locations = self.initial_data.pop('locations')
    #     return super().is_valid(raise_exception=raise_exception)

    def save(self):
        author = super().save()
        locations = self.initial_data.get('locations')
        if locations:
            for location_name in locations:
                # Cоединились по слагфилд и теперь не создаст если не существует locations.name, как подправить?
                location, _ = Location.objects.get_or_create(name=location_name)
                author.locations.add(location)
        author.save()
        return author


class AuthorDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id']


class AdvDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']
