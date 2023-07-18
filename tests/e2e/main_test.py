import json
from pathlib import Path

from laptop_scraper.__main__ import main


def test_lenovo_ordered_by_price(tmp_path: Path) -> None:
    file = tmp_path / "products.json"
    main(["-b", "lenovo", "-o", "price", "-f", file.as_posix()])

    file_content = json.load(file.open())
    with open("tests/mocks/e2e/lenovo_ordered_by_price.json") as mock_file:
        assert file_content == json.load(mock_file)
