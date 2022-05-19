from django.db.models import Q
from django.views.generic import UpdateView
from django.utils import timezone
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import ADFilter, ArticleFilter
from ads.models import Ad, Category, Location, Selection, Comment
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from ads.permissions import SelectionUpdateDeletePermission, \
    CommentsUpdateDeletePermission
from ads.serializers import LocationSerializer, ADVListSerializer, CategorySerializer, AdvDestroySerializer, \
    ADVCreateSerializer, ADVUpdateSerializer, SelectionRetrieveSerializer, SelectionListSerializer, \
    SelectionUpdateSerializer, SelectionDestroySerializer, SelectionCreateSerializer, CommentsListSerializer, \
    CommentCreateSerializer, CommentUpdateSerializer, CommentDestroySerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter


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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ADFilter

    @extend_schema(
        description="Retrieve adv list",
        summary="adv list",
        parameters=[
            OpenApiParameter(name='category__id', description='Filter by id of category', required=False, type=str),
            OpenApiParameter(name='name__icontains', description='Filter by name if name contains value',
                             required=False, type=str),
            OpenApiParameter(name='price__gt', description='Filter by price__gt if price__gt > value', required=False,
                             type=int),
            OpenApiParameter(name='price__lt', description='Filter by price__lt if price__lt < value', required=False,
                             type=int),
            OpenApiParameter(name='price', description='Filter by price if price equal value', required=False,
                             type=int)]
    )
    # TODO всегда придется писать get?
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdvMeAPIView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = ADVListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArticleFilter
    permission_classes = [IsAuthenticated, ]

    # TODO был ли смысл делать фильтр в filters.py?
    # def get(self, request, *args, **kwargs):
    #     self.queryset = self.queryset.filter(
    #         Q(author__id__exact=request.user.id)
    #     )
    #     return super().get(request, *args, **kwargs)


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


class AdCommentsListViewAPI(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(
            Q(ad_id__id__exact=kwargs['pk'])
        )
        return super().get(request, *args, **kwargs)


# TODO как сделать по другому?
class AdCommentsRetrieveViewAPI(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(
            Q(ad_id__id__exact=kwargs['pk']) & Q(id__exact=kwargs['commentId'])
        )
        return super().get(request, *args, **kwargs)


class CommentRetrieveViewAPI(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer
    permission_classes = [IsAuthenticated]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated, CommentsUpdateDeletePermission]

    # Вкусовщина, просто чтобы менялась дата создания при обновлении, так же пользователь,
    # не может задать свою дату.
    def patch(self, request, *args, **kwargs):
        request.data['created_at'] = timezone.now()
        return super().patch(request, *args, **kwargs)


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    permission_classes = [IsAuthenticated, CommentsUpdateDeletePermission]
