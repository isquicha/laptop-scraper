from bs4 import BeautifulSoup

from .constants import BRANDS
from .entities import Product


def get_product_name(div: BeautifulSoup) -> str:
    return div.find("a", {"class": "title"}).text or ""


def get_product_brand(product_name: str) -> str:
    for brand_slug, brand_name in BRANDS.items():
        if brand_slug in product_name.lower():
            return brand_name
    return ""


def get_product_price(div: BeautifulSoup) -> float:
    return float(
        div.find("h4", {"class": "pull-right price"}).text.replace("$", "")
    )


def get_product_description(div: BeautifulSoup) -> str:
    return div.find("p", {"class": "description"}).text or ""


def get_product_rating(div: BeautifulSoup) -> float:
    ratings_div = div.find("div", {"class": "ratings"})
    ratings_paragraphs = ratings_div.find_all("p")
    rating_holder = ratings_paragraphs[-1]
    rating = rating_holder["data-rating"]
    return rating or 0.0


def get_product_reviews(div: BeautifulSoup) -> str:
    return div.find("p", {"class": "pull-right"}).text or ""


def get_product_image(div: BeautifulSoup) -> str:
    relative_url = div.find("img", {"class": "img-responsive"})["src"] or ""
    return f"https://webscraper.io{relative_url}"


def get_product_url(div: BeautifulSoup) -> str:
    relative_url = div.find("a", {"class": "title"})["href"] or ""
    return f"https://webscraper.io{relative_url}"


def scrape_page(page_content: str) -> list[Product]:
    soup = BeautifulSoup(page_content, "html.parser")
    header = soup.find("h1", {"class": "page-header"})
    products_div = header.parent.div

    return [
        {
            "name": get_product_name(div),
            "brand": get_product_brand(get_product_name(div)),
            "price": get_product_price(div),
            "description": get_product_description(div),
            "rating": get_product_rating(div),
            "reviews": get_product_reviews(div),
            "image": get_product_image(div),
            "url": get_product_url(div),
        }
        for div in products_div.find_all(
            "div", {"class": "col-sm-4 col-lg-4 col-md-4"}
        )
    ]
