import pytest
from bs4 import BeautifulSoup

from laptop_scraper.scraper import get_product_name


@pytest.mark.parametrize(
    "index, expected", [(1, "Asus VivoBook X4..."), (2, "Prestigio SmartB...")]
)
def test_get_product_name(index: int, expected: str) -> None:
    with open(f"tests/mocks/unit/product_{index}_div.html") as file:
        given_content = file.read()
    given_content = BeautifulSoup(given_content, "html.parser")
    assert get_product_name(given_content) == expected
