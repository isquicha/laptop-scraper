import json
import sys
from argparse import ArgumentParser, Namespace
from typing import Sequence

import requests

from .constants import BRANDS, URL
from .scraper import scrape_page


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


def main(args_to_parse: Sequence[str] = sys.argv[1:]) -> None:
    args = parse_args(args_to_parse)
    result = requests.get(args.url)
    products = scrape_page(result.text)

    if args.brand:
        products = [
            product for product in products if product["brand"] == args.brand
        ]

    products.sort(
        key=lambda product: product[args.order],  # type:ignore
        reverse=args.reverse,
    )

    with open(args.file, "w") as file:
        json.dump(products, file, indent=4)


if __name__ == "__main__":
    main()
