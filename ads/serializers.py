from ads.Validators import status, ADVNotInStatusValidator
from ads.models import Location, Ad, Category, Selection
from users.models import User
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
        model = User
        fields = ["username", "locations", "role"]


class ADVListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False,
                                            required=False,
                                            slug_field='name',
                                            queryset=Category.objects.all()
                                            )

    # author = AuthorSerializer()
    author = serializers.SlugRelatedField(many=False,
                                          required=False,
                                          slug_field='username',
                                          queryset=User.objects.all()
                                          )

    class Meta:
        model = Ad
        fields = ['id', 'name', 'price', 'image', 'author', 'category', 'is_published']


class ADVCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    author = serializers.SlugRelatedField(many=False,
                                          required=False,
                                          slug_field='username',
                                          queryset=User.objects.all()
                                          )

    is_published = serializers.CharField(max_length=13, default=False,
                                         validators=[ADVNotInStatusValidator(["TRUE", "True"])])

    class Meta:
        model = Ad
        fields = ['id', 'name', 'price', 'category', 'author', 'image', 'is_published']

    def is_valid(self, raise_exception=False):
        # Словарь который передает пользователь
        self._author = self.initial_data.pop('author', None)
        return super().is_valid(raise_exception=raise_exception)

    # Не нужен цикл ведь мы находимся не ManytoManyField поэтому там нет массива
    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        if self._author:
            author, _ = User.objects.get_or_create(username=self._author)
            # Здесь вместо Add решил написать так.
            ad.author = author
        ad.save()
        return ad


class ADVUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)

    author = serializers.SlugRelatedField(many=False,
                                          required=False,
                                          slug_field='username',
                                          queryset=User.objects.all()
                                          )

    class Meta:
        model = Ad
        fields = ['id', 'name', 'price', 'category', 'author', 'image']

    def is_valid(self, raise_exception=False):
        # Словарь который передает пользователь
        self._author = self.initial_data.get('author', None)
        return super().is_valid(raise_exception=raise_exception)

    # Не нужен цикл ведь мы находимся не ManytoManyField поэтому там нет массива
    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        if self._author:
            author, _ = User.objects.get_or_create(username=self._author)
            # Здесь вместо Add решил написать так.
            ad.author = author
        ad.save()
        return ad


class AdvDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']




class ADVListSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        exclude = ['owner', 'items']
        ordering = ['id']
        # fields = '__all__'


class SelectionRetrieveSerializer(serializers.ModelSerializer):
    items = ADVListSelectionSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


# Помнить что сериалайзер отвечает не только за отображение но и за доступ к полям
# В данном случае исключим owner чтобы невозможно было его поменять при Update.
class SelectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        ordering = ['id']
        exclude = ['owner']


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        ordering = ['id']
        fields = '__all__'


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        ordering = ['id']
        fields = ['id']
