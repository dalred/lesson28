import pytest
from ads.serializers import SelectionRetrieveSerializer, SelectionListSerializer, SelectionCreateSerializer
from tests.factories import SelectionFactory


@pytest.mark.django_db
def test_retrieve_selection(client, selection, jwt_admin_token):
    response = client.get(f"/selections/{selection.pk}/", HTTP_AUTHORIZATION="Bearer " + jwt_admin_token)
    assert response.status_code == 200
    assert response.data == SelectionRetrieveSerializer(selection).data


@pytest.mark.django_db
def test_get_all_selection(client, jwt_admin_token):
    selection = SelectionFactory.create_batch(3, items=1)
    response = client.get("/selections/", HTTP_AUTHORIZATION="Bearer " + jwt_admin_token)
    assert response.status_code == 200
    assert response.data == SelectionListSerializer(selection, many=True).data


@pytest.mark.django_db
def test_post_selection(client, ad, jwt_admin_token):
    # Owner не передается так как он создается в SelectionCreateAPIView
    data = {
        "name": "test подборка",
        "items": [ad.pk],
    }
    response = client.post("/selection/create/", data=data, content_type='application/json',
                           HTTP_AUTHORIZATION="Bearer " + jwt_admin_token)
    serializer = SelectionCreateSerializer(data=response.data)
    assert response.status_code == 201
    assert serializer.is_valid(raise_exception=True)
