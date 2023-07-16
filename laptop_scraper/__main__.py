import json
from dataclasses import asdict, dataclass

import requests
from bs4 import BeautifulSoup

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"


@dataclass
class Product:
    name: str
    price: float
    description: str
    rating: float
    reviews: str
    image: str
    url: str

    def __gt__(self, other: "Product") -> bool:
        return self.price > other.price


def get_product_from_div(div: BeautifulSoup) -> Product:
    name = div.find("a", {"class": "title"}).text
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
    return Product(name, price, description, rating, reviews, image, url)


def main() -> None:
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    header = soup.find("h1", {"class": "page-header"})
    products_div = header.parent.div

    products = [
        get_product_from_div(div)
        for div in products_div.find_all(
            "div", {"class": "col-sm-4 col-lg-4 col-md-4"}
        )
    ]

    products.sort()
    lenovo_products = [
        product for product in products if "lenovo" in product.name.lower()
    ]
    with open("lenovo.json", "w") as f:
        json.dump([asdict(p) for p in lenovo_products], f, indent=2)
