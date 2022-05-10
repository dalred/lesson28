
import factory.fuzzy
from ads.models import Ad, Category, Location, Selection
from users.models import User




class CategoryFactory(factory.django.DjangoModelFactory):
    #TODO не смог навесить ограничение по количеству знаков которые используются для модели.
    name = "testname"
    class Meta:
        model = Category

class LocationFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("address")
    #factory.Sequence если нужно уникальные.
    class Meta:
        model = Location

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")

    @factory.post_generation
    def locations(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for _ in range(extracted):
                self.locations.add(LocationFactory())


class AdvFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    price = factory.fuzzy.FuzzyInteger(0, 42)
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(AuthorFactory)
    is_published = "FALSE"

    class Meta:
        model = Ad

class SelectionFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    owner = factory.SubFactory(AuthorFactory)

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for _ in range(extracted):
                self.items.add(AdvFactory())

    class Meta:
        model = Selection