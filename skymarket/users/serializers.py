from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db.models import Q
from ads.Validators import UserCreateCheckbirth_date, UserCreateEmailDomen, UserCreateAge
from ads.models import Location
from djoser import serializers as djoser_serializers
from django.contrib.auth import get_user_model

from users.models import User

Author = get_user_model()


class AuthorCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True,
                                             required=False,
                                             slug_field='name',
                                             queryset=Location.objects.all()
                                             )
    image = serializers.ImageField(max_length=None, allow_null=True, use_url=True, required=False)
    age = serializers.IntegerField(validators=[UserCreateAge()])
    role = serializers.CharField(allow_null=False)
    birth_date = serializers.DateField(validators=[UserCreateCheckbirth_date], required=False)
    # Проверка переданного пользователем поля email, в выборке где поле email is NOT NULL
    # lookup можно так же использовать and database.user.email = or like user.post.data.email то есть дополнительное
    # условие по вхождению поля от пользователя с заданными условиями, где пригодится непонятно.
    # условие по вхождению поля от пользователя с заданными условиями, где пригодится непонятно.
    emails_q = ~Q(email__exact=None)
    email = serializers.EmailField(allow_null=False,
                                   validators=[UniqueValidator(queryset=User.objects.filter(emails_q)),
                                               UserCreateEmailDomen])

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

        author.set_password(validated_data["password"])
        author.save()
        return author


class AuthorUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_null=True, use_url=True, required=False)
    locations = serializers.SlugRelatedField(many=True,
                                             required=False,
                                             slug_field='name',
                                             queryset=Location.objects.all()
                                             )
    email = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'role', 'age', 'locations', 'image']

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
                # TODO Cоединились по слагфилд и теперь не создаст если не существует locations.name, как подправить?
                location, _ = Location.objects.get_or_create(name=location_name)
                author.locations.add(location)
        author.save()
        return author


class AuthorDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id']


class AuthorListSerializer(serializers.ModelSerializer):
    # Чтобы отразить locations по name, при этому locations.name уникальное.
    # Чтобы отразить locations по id, при этому locations.id уникальное(slug_field='id').
    locations = serializers.SlugRelatedField(many=True,
                                             read_only=True,
                                             slug_field='name'
                                             )

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "phone", "locations"]


class AuthorCurrentSerializer(djoser_serializers.UserSerializer):
    """
        Uses extra user model's fields in /me/ endpoint.
    """
    class Meta(djoser_serializers.UserSerializer.Meta):
        fields = djoser_serializers.UserSerializer.Meta.fields + (
            'first_name',
            'last_name',
            'phone',
        )