from django.db.models import Q

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ads.filters import UserFilter
from users.serializers import AuthorCreateSerializer, AuthorUpdateSerializer, AuthorDestroySerializer, AuthorListSerializer
from users.models import User
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class AuthorListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = [IsAuthenticated]


class AuthorRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorListSerializer


# class AuthorPublishedAPIView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = AuthorListSerializer
#
#     def get(self, request, *args, **kwargs):
#         is_published = request.GET.get("is_published", None)
#
#         if is_published:
#             self.queryset = self.queryset.filter(
#                 Q(ad__is_published__exact=is_published)
#             )
#
#         return super().get(request, *args, **kwargs)

class AuthorPublishedAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter

    @extend_schema(
        description="Retrieve AuthorPublished or Not",
        summary="Is Author published?",
        parameters=[
            OpenApiParameter(name='ad__is_published', description='Filter by ad is_published TRUE or FALSE', required=True, type=str)]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




class AuthorCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorCreateSerializer


class AuthorUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorUpdateSerializer


class AuthorDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorDestroySerializer