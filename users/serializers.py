from rest_framework import serializers

from ads.models import Location

from django.contrib.auth import get_user_model

Author = get_user_model()



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

        author.set_password(validated_data["password"])
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