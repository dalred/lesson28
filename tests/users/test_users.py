import pytest
from ads.serializers import AuthorSerializer
from tests.factories import AuthorFactory, LocationFactory
from users.models import User


@pytest.mark.django_db
def test_list_users(client, jwt_admin_token):
    # [] Потому что ожидается List, а не одна запись.
    # expected_response = [{
    #     "username": "username",
    #     "locations": [
    #     ],
    #     "role": "admin"
    # }]
    #TODO покажите свои примеры для связи many to many
    # locations в данном случае количество локаций
    author = AuthorFactory.create_batch(5, locations=1)
    queryset = User.objects.all()
    response = client.get(f"/users/", HTTP_AUTHORIZATION="Bearer " + jwt_admin_token)
    assert response.status_code == 200
    assert response.data == AuthorSerializer(queryset, many=True).data
