import json
from django.views.generic import UpdateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category, Author, Location
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Q
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from django.db.models import Max
from ads.serializers import LocationSerializer, AuthorSerializer, AuthorCreateSerializer, \
    AuthorDestroySerializer, AuthorUpdateSerializer, ADVListSerializer, CategorySerializer, AdvDestroySerializer, \
    ADVCreateSerializer


def root(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({
        "status": "ok"
    })


class ADVCreateViewSet(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = ADVCreateSerializer

class ADVListViewSet(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = ADVListSerializer

    def get(self, request, *args, **kwargs):
        cat = request.GET.get("cat", None)
        text = request.GET.get("text", None)
        location = request.GET.get("location", None)
        price_to = request.GET.get("price_to", self.queryset.aggregate(Max('price'))['price__max'])
        price_from = request.GET.get("price_from", None)
        if cat:
            self.queryset = self.queryset.filter(
                Q(category__id__exact=cat)
            )
        if text:
            self.queryset = self.queryset.filter(
                Q(name__icontains=text)
            )
        if location:
            self.queryset = self.queryset.filter(
                Q(author__location_id__name__icontains=location)
            )

        if price_from:
            self.queryset = self.queryset.filter(Q(price__range=[price_from, price_to]))
        return super().get(request, *args, **kwargs)

class AdvRetrieveView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = ADVListSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdvUpdateView(UpdateView):
    model = Ad
    fields = ["name", "author_id", "price", "description", "category_id"]

    # Создает если нет, обновляет если есть
    def patch(self, request: WSGIRequest, pk) -> JsonResponse:
        adv_data = json.loads(request.body)
        adv, _ = self.model.objects.update_or_create(
            id=pk,
            defaults={
                "name": adv_data['name'],
                "author_id": adv_data['author_id'],
                "price": adv_data['price'],
                "description": adv_data['description'],
                "category_id": adv_data['category_id']
            }
        )
        adv.save()
        return JsonResponse({
            "id": adv.id,
            "name": adv.name,
            "author_id": adv.author_id,
            "price": adv.price,
            "description": adv.description,
            "category_id": adv.category_id
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdvUpdateImageView(UpdateView):
    model = Ad
    fields = ["name", "author_id", "price", "description", "category_id"]

    def post(self, request: WSGIRequest, *args, **kwargs) -> JsonResponse:
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        })


class AdvDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdvDestroySerializer


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorPublishedAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        is_published = request.GET.get("is_published", None)

        if is_published:
            self.queryset = self.queryset.filter(
                Q(ad__is_published__exact=is_published)
            )

        return super().get(request, *args, **kwargs)

class AuthorCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer


class AuthorUpdateView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorUpdateSerializer


class AuthorDeleteView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDestroySerializer


# Наверное имелся ввиду просто ViewSet, но я пасс, я разобрался)
class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



class CatViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['id']
