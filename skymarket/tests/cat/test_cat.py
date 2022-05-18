import pytest
from skymarket.ads.serializers import CategorySerializer

@pytest.mark.django_db
def test_retrieve_cat(client, category, jwt_admin_token):
    response = client.get(f"/cat/{category.pk}/", HTTP_AUTHORIZATION="Bearer " + jwt_admin_token)
    assert response.status_code == 200
    assert response.data == CategorySerializer(category).data