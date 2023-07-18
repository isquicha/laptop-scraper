from json import loads

from laptop_scraper.scraper import scrape_page


def test_scrape_full_page() -> None:
    with open("tests/mocks/integration/full_page.html") as file:
        given_content = file.read()
    with open("tests/mocks/integration/full_page_content.json") as file:
        expected_content = loads(file.read())
    assert scrape_page(given_content) == expected_content
