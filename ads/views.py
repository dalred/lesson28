from django.views.generic import UpdateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category, Location, Selection
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db.models import Max
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from ads.permissions import SelectionUpdateDeletePermission, SelectionCheckRolePermission
from ads.serializers import LocationSerializer, ADVListSerializer, CategorySerializer, AdvDestroySerializer, \
    ADVCreateSerializer, ADVUpdateSerializer, SelectionRetrieveSerializer, SelectionListSerializer, \
    SelectionUpdateSerializer, SelectionDestroySerializer, SelectionCreateSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

def root(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({
        "status": "ok"
    })


# Category по id, Authors по username
class ADVCreateViewSet(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = ADVCreateSerializer


class ADVUpdateViewSet(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = ADVUpdateSerializer


class ADVListViewSet(ListAPIView):

    queryset = Ad.objects.all()
    serializer_class = ADVListSerializer

    @extend_schema(
        description="Retrieve adv list",
        summary="adv list"
    )

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
        # Поиск по полю name
        if text:
            self.queryset = self.queryset.filter(
                Q(name__icontains=text)
            )
        #Поиск по вложенным полям таблицы author
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


# Наверное имелся ввиду просто ViewSet, но я пасс, я разобрался)
class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CatViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['id']




class SelectionListViewAPI(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer

# Детальный просмотр только от авторизованных пользователей.
@permission_classes([IsAuthenticated])
class SelectionRetrieveViewAPI(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionRetrieveSerializer


class SelectionCreateAPIView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated, SelectionUpdateDeletePermission]

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        return super().create(request, *args, **kwargs)


# Логические операции в permissions доступны только для одинаковых методов LAL
class SelectionUpdateAPIView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionUpdateDeletePermission]


class SelectionDeleteAPIView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDestroySerializer
    permission_classes = [IsAuthenticated, SelectionUpdateDeletePermission]
