import json
import sys
from argparse import ArgumentParser, Namespace
from typing import Sequence, TypedDict

import requests
from bs4 import BeautifulSoup

from .constants import BRANDS, URL


class Product(TypedDict):
    name: str
    brand: str
    price: float
    description: str
    rating: float
    reviews: str
    image: str
    url: str


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


def parse_args(args_to_parse: Sequence[str]) -> Namespace:
    parser = ArgumentParser(
        prog="Laptop Scraper", description="Scrape laptops from webscraper.io"
    )

    parser.add_argument(
        "-u", "--url", default=URL, help="URL to scrape", required=False
    )
    parser.add_argument(
        "-b",
        "--brand",
        choices=set(BRANDS.values()),
        default=None,
        help="Brand to filter by",
        required=False,
    )
    parser.add_argument(
        "-o",
        "--order",
        choices=["price", "name", "brand", "rating", "reviews"],
        default="name",
        help="Order results by",
        required=False,
    )
    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="Reverse the order of results",
        required=False,
    )
    parser.add_argument(
        "-f",
        "--file",
        default="products.json",
        help="File to save results to",
        required=False,
    )

    return parser.parse_args(args_to_parse)


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


def main(args_to_parse: Sequence[str] = sys.argv[1:]) -> None:
    args = parse_args(args_to_parse)
    result = requests.get(args.url)
    products = scrape_page(result.text)

    if args.brand:
        products = [
            product for product in products if product["brand"] == args.brand
        ]

    products = sorted(
        products,
        key=lambda product: product[args.order],  # type:ignore
        reverse=args.reverse,
    )

    with open(args.file, "w") as file:
        json.dump(products, file, indent=4)


if __name__ == "__main__":
    main()
