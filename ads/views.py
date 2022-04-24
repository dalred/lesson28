import json
from django.conf import settings
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.http import JsonResponse
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category, Author, Location
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db.models import Count
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.generics import ListAPIView

from ads.serializers import LocationSerializer


def root(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({
        "status": "ok"
    })


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request: WSGIRequest) -> JsonResponse:
        # По мне так себе затея с select_related, по логам запрос огромный
        ads = Ad.objects.select_related("author").select_related("category").all()

        paginator = Paginator(ads, settings.TOTAL_ON_PAGE)
        # Не совсем понял зачем по умолчанию нужно было возвращать 0(в шпаргалке), так же неудобно
        # Будет выдаваться последняя страница если не указан page
        page_number = int(request.GET.get("page", 1))  # Забираем query-параметр page
        page_obj = paginator.get_page(page_number)

        response = []
        for ad in page_obj:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "image": ad.image.url
            })

        return JsonResponse({
            "items": response,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
            "page_number": page_number,
        }, safe=False, status=200)

    def post(self, request: WSGIRequest) -> JsonResponse:
        ad_data = json.loads(request.body)
        ad, _ = Ad.objects.get_or_create(name=ad_data["name"])

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url
        })


class AdvDetailView(View):
    def get(self, request: WSGIRequest, pk) -> JsonResponse:
        adv = get_object_or_404(Ad, id=pk)

        return JsonResponse({
            "id": adv.id,
            "name": adv.name,
            "author_id": adv.author_id,
            "price": adv.price,
            "description": adv.description,
            "is_published": adv.is_published,
            "category_id": adv.category_id,
            "image": adv.image.url
        }, status=200)


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


@method_decorator(csrf_exempt, name='dispatch')
class AdvDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request: WSGIRequest, *args, **kwargs) -> JsonResponse:
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request: WSGIRequest) -> JsonResponse:
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, status=200)

    def post(self, request: WSGIRequest) -> JsonResponse:
        category_data = json.loads(request.body)
        # Метод get_or_create() способен вернуть только одну запись,
        # удовлетворяющую заданным критериям поиска
        category, _ = Category.objects.get_or_create(name=category_data["name"])

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(View):
    model = Category

    def get(self, request: WSGIRequest, pk) -> JsonResponse:
        category = get_object_or_404(Category, id=pk)

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    # Создает если нет, обновляет если есть
    def patch(self, request: WSGIRequest, pk) -> JsonResponse:
        category_data = json.loads(request.body)
        category, _ = self.model.objects.update_or_create(
            id=pk,
            defaults={
                "name": category_data["name"]
            }
        )
        category.save()
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request: WSGIRequest, *args, **kwargs) -> JsonResponse:
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AuthorView(View):
    model = Author
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age']

    def get(self, request: WSGIRequest) -> JsonResponse:
        response = []
        users = self.model.objects.all()
        paginator = Paginator(users, settings.TOTAL_ON_PAGE)
        # Не совсем понял зачем по умолчанию нужно было возвращать 0(в шпаргалке), так же неудобно
        # Будет выдаваться последняя страница если не указан page
        page_number = int(request.GET.get("page", 1))  # Забираем query-параметр page
        page_obj = paginator.get_page(page_number)

        for user in page_obj:
            response.append(
                {
                    "id": user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'password': user.password,
                    'role': user.role,
                    'age': user.age,
                    'locations': [location.name for location in user.location_id.all()],
                }
            )
        return JsonResponse({
            "items": response,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
            "page_number": page_number,
        }, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AuthorDetailView(View):
    model = Author

    def get(self, request: WSGIRequest, pk) -> JsonResponse:
        user = get_object_or_404(self.model, id=pk)
        # user = user.filter(ad__is_published='TRUE').annotate(count=Count("ad")).get()
        return JsonResponse({
            "id": user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': user.password,
            'role': user.role,
            'age': user.age,
            'locations': [location.name for location in user.location_id.all()],
        }, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AuthorPublishedView(ListView):
    model = Author
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age']

    def get(self, request: WSGIRequest, *args, **kwargs) -> JsonResponse:
        super().get(request, *args, **kwargs)
        # Здесь непонятно как проще сделать и в задании маршрут как-то невнятно указан.
        users = self.object_list.filter(pk=kwargs.get('pk', 1), ad__is_published='TRUE').annotate(total_ads=Count("ad"))
        response = []

        for user in users:
            response.append(
                {
                    "id": user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'password': user.password,
                    'role': user.role,
                    'age': user.age,
                    'total_ads': user.total_ads,
                    'locations': [location.name for location in user.location_id.all()],
                }
            )
        return JsonResponse(response, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AuthorCreateView(CreateView):
    def post(self, request: WSGIRequest, *args, **kwargs) -> JsonResponse:
        user_data = json.loads(request.body)

        # Метод get_or_create() способен вернуть только одну запись, defaults поле по умолчанию
        # удовлетворяющую заданным критериям поиска
        user, _ = Author.objects.get_or_create(
            username=user_data["username"],
            password=user_data["password"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            age=user_data["age"],
        )
        for location_name in user_data["locations"]:
            location, _ = Location.objects.get_or_create(name=location_name)
            user.location_id.add(location)

        return JsonResponse({
            "id": user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': user.password,
            'role': user.role,
            'age': user.age,
            'locations': [location.name for location in user.location_id.all()],
        }, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AuthorDeleteView(DeleteView):
    model = Author
    success_url = "/"

    def delete(self, request: WSGIRequest, *args, **kwargs) -> JsonResponse:
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age']

    # Создает если нет, обновляет если есть
    def patch(self, request: WSGIRequest, pk) -> JsonResponse:
        user_data = json.loads(request.body)
        user, _ = Author.objects.update_or_create(
            id=pk,
            defaults={
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'username': user_data['username'],
                'password': user_data['password'],
                'role': user_data['role'],
                'age': user_data['age'],
            }
        )
        for location_name in user_data["locations"]:
            # Вариантов тут несколько:
            # 1) Пользователь добавляет в локации пользователя существующую локацию - filter(),
            # 2) Пользователь добавляет в локации пользователя новую локацию .get_or_create(name=location_name)
            # 3) Пользователь хочет заменить(set) локацию пользователя существующей локацией
            # 4) Пользователь хочет заменить(set) локацию пользователя существующей или новой локацией
            # выбрал 2й вариант
            location, _ = Location.objects.all().get_or_create(name=location_name)
            user.location_id.add(location)
        user.save()
        return JsonResponse({
            "id": user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': user.password,
            'role': user.role,
            'age': user.age,
            'locations': [location.name for location in user.location_id.all()],
        }, safe=False, status=200)


class LocationListView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
