import pytest

from tests.factories import AdvFactory
from ads.serializers import ADVListSerializer, ADVCreateSerializer
from my_project.settings import REST_FRAMEWORK

REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'] = None


@pytest.mark.django_db
def test_retrieve_adv(client):
    adv = AdvFactory.create()
    response = client.get(f"/ad/{adv.pk}/")
    assert response.status_code == 200
    assert response.data == ADVListSerializer(adv).data


@pytest.mark.django_db
def test_get_all_adv(client):
    adv = AdvFactory.create_batch(3)
    response = client.get("/ad/")
    assert response.status_code == 200
    assert response.data == ADVListSerializer(adv, many=True).data


@pytest.mark.django_db
def test_post_adv(client, category):
    data = {
        "name": "Сибирская котята тест тест, 3 месяца",
        "price": 2500,
        "author": "pnikifirov",
        "category": category.id,
        "is_published": "FALSE"
    }
    response = client.post("/ad/create/", data=data, content_type='application/json')
    print(response.json())
    serializer = ADVCreateSerializer(data=response.data)
    assert response.status_code == 201
    assert serializer.is_valid(raise_exception=True)
