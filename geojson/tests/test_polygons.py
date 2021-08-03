import json

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from model_bakery import baker
from moneyed import Money as OldMoney


@pytest.mark.django_db
def test_polygon_list(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    money = OldMoney(1, "USD")

    polygon = baker.make(
        "polygons.Polygon",
        provider=provider,
        name="test1",
        is_active=True,
        price=money,
    )

    url = reverse("polygon-list")
    res = client.get(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["count"] == 1
    assert res.json()["results"][0]["id"] == polygon.id


@pytest.mark.django_db
def test_polygon_list_return_only_active(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    money = OldMoney(1, "USD")

    baker.make(
        "polygons.Polygon",
        provider=provider,
        name="test1",
        is_active=False,
        price=money,
    )

    polygon2 = baker.make(
        "polygons.Polygon",
        provider=provider,
        name="test2",
        is_active=True,
        price=money,
    )

    url = reverse("polygon-list")
    res = client.get(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["count"] == 1
    assert res.json()["results"][0]["id"] == polygon2.id


@pytest.mark.django_db
def test_polygon_list_search(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    money = OldMoney(1, "USD")

    polygon1 = baker.make(
        "polygons.Polygon",
        provider=provider,
        name="test1",
        is_active=True,
        price=money,
        lat=1.10,
        lng=1.10,
    )

    polygon2 = baker.make(
        "polygons.Polygon",
        provider=provider,
        name="test2",
        is_active=True,
        price=money,
        lat=2.00,
        lng=2.00,
    )

    url = reverse("polygon-list")
    url = f"{url}?lat={1.10}&lng={1.10}"
    res = client.get(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["count"] == 1
    assert res.json()["results"][0]["id"] == polygon1.id


@pytest.mark.django_db
def test_polygon_list_should_include_provider(client):
    provider = baker.make(
        "providers.Provider", name="test1", phone_number="+911234567890", is_active=True
    )

    money = OldMoney(1, "USD")

    polygon = baker.make(
        "polygons.Polygon",
        provider=provider,
        name="test1",
        is_active=True,
        price=money,
    )

    url = reverse("polygon-list")
    res = client.get(
        url,
        content_type="application/json",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["count"] == 1
    assert res.json()["results"][0]["id"] == polygon.id
    assert res.json()["results"][0]["provider"]["id"] == provider.id
    assert res.json()["results"][0]["provider"]["name"] == provider.name


# add more tests to test crud
