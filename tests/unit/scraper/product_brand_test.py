import pytest

from laptop_scraper.scraper import get_product_brand


@pytest.mark.parametrize(
    "product_name, expected",
    [
        ("Asus VivoBook X4...", "asus"),
        ("Prestigio SmartB...", "prestigio"),
        ("ThinkPad Yoga", "lenovo"),
    ],
)
def test_get_product_brand(product_name: str, expected: str) -> None:
    assert get_product_brand(product_name) == expected
