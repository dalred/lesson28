from django.db.models import Q

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ads.serializers import AuthorSerializer
from users.serializers import AuthorCreateSerializer, AuthorUpdateSerializer, AuthorDestroySerializer
from users.models import User
from rest_framework.permissions import IsAuthenticated

class AuthorListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, ]


class AuthorRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class AuthorPublishedAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        is_published = request.GET.get("is_published", None)

        if is_published:
            self.queryset = self.queryset.filter(
                Q(ad__is_published__exact=is_published)
            )

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