from bs4 import BeautifulSoup

from .constants import BRANDS
from .entities import Product


def get_product_from_div(div: BeautifulSoup) -> Product:
    name = div.find("a", {"class": "title"}).text
    brand = ""
    for brand_slug, brand_name in BRANDS.items():
        if brand_slug in name.lower():
            brand = brand_name
            break
    price = float(
        div.find("h4", {"class": "pull-right price"}).text.replace("$", "")
    )
    description = div.find("p", {"class": "description"}).text
    rating = div.find("div", {"class": "ratings"}).find_all("p")[-1][
        "data-rating"
    ]
    reviews = div.find("p", {"class": "pull-right"}).text
    image = div.find("img", {"class": "img-responsive"})["src"]
    image = f"https://webscraper.io{image}"
    url = div.find("a", {"class": "title"})["href"]
    url = f"https://webscraper.io{url}"
    return {
        "name": name,
        "brand": brand,
        "price": price,
        "description": description,
        "rating": rating,
        "reviews": reviews,
        "image": image,
        "url": url,
    }


def scrape_page(page_content: str) -> list[Product]:
    soup = BeautifulSoup(page_content, "html.parser")
    header = soup.find("h1", {"class": "page-header"})
    products_div = header.parent.div

    return [
        get_product_from_div(div)
        for div in products_div.find_all(
            "div", {"class": "col-sm-4 col-lg-4 col-md-4"}
        )
    ]
