import datetime
import pytest
from unittest.mock import patch, Mock
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@patch("app.main.datetime.date", wraps=datetime.date)
def test_outdated_products(mock_date: Mock, products: list) -> None:
    mock_date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]


@patch("app.main.datetime.date", wraps=datetime.date)
def test_outdated_products_not_expired(mock_date: Mock,
                                       products: list) -> None:
    mock_date.today.return_value = datetime.date(2022, 2, 1)
    result = outdated_products(products)
    assert result == []
