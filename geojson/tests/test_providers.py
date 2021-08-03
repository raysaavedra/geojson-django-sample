import json

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from model_bakery import baker


@pytest.mark.django_db
def test_provider_list(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    url = reverse("provider-list")
    res = client.get(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["count"] == 1
    assert res.json()["results"][0]["id"] == provider.id


@pytest.mark.django_db
def test_provider_list_return_only_active(client):
    baker.make(
        "providers.Provider",
        name="test1",
        phone_number="+911234567890",
        is_active=False,
    )
    provider2 = baker.make(
        "providers.Provider", name="test2", phone_number="+911234567890", is_active=True
    )
    baker.make(
        "providers.Provider", name="test3", phone_number="+911234567890", is_active=True
    )

    url = reverse("provider-list")
    res = client.get(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["count"] == 2
    assert res.json()["results"][0]["id"] == provider2.id


@pytest.mark.django_db
def test_provider_get(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    url = reverse("provider-detail", args=[provider.id])
    res = client.get(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["id"] == provider.id


@pytest.mark.django_db
def test_provider_delete(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    url = reverse("provider-detail", args=[provider.id])
    res = client.delete(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_provider_update(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    url = reverse("provider-detail", args=[provider.id])

    res = client.put(
        url,
        json.dumps(
            {
                "name": "test2",
            }
        ),
        content_type="application/json",
    )

    assert res.status_code == status.HTTP_200_OK
    assert res.json()["name"] == "test2"


@pytest.mark.django_db
def test_provider_create(client):
    url = reverse("provider-list")

    res = client.post(
        url,
        json.dumps(
            {
                "name": "test1",
                "email": "test@test.com",
                "phone_number": "+911234567890",
                "is_active": True,
            }
        ),
        content_type="application/json",
    )

    assert res.status_code == status.HTTP_201_CREATED
    assert res.json()["name"] == "test1"
