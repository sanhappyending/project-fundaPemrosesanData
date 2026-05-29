import os
import sys
import unittest

from unittest.mock import patch
from bs4 import BeautifulSoup

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from utils.extract import (
    extract_store_products,
    scrape_store_products
)


class TestStoreProductExtraction(unittest.TestCase):

    def setUp(self):

        self.sample_html = """
        <div class="collection-card">

            <h3>T-shirt 2</h3>

            <div class="price-container">
                <span class="price">$102.15</span>
            </div>

            <div class="product-details">
                <p>Rating: ⭐ 3.9 / 5</p>
                <p>3 Colors</p>
                <p>Size: M</p>
                <p>Gender: Women</p>
            </div>

        </div>
        """

        self.invalid_html = """
        <div class="collection-card"></div>
        """

    def test_extract_store_products_success(self):

        soup = BeautifulSoup(
            self.sample_html,
            "html.parser"
        )

        item = soup.find(
            "div",
            class_="collection-card"
        )

        result = extract_store_products(item)

        self.assertEqual(
            result["Title"],
            "T-shirt 2"
        )

        self.assertEqual(
            result["Price"],
            "$102.15"
        )

        self.assertEqual(
            result["Rating"],
            "Rating: ⭐ 3.9 / 5"
        )

        self.assertEqual(
            result["Colors"],
            "3 Colors"
        )

        self.assertEqual(
            result["Size"],
            "Size: M"
        )

        self.assertEqual(
            result["Gender"],
            "Gender: Women"
        )

        self.assertIn(
            "Timestamp",
            result
        )

    def test_extract_store_products_invalid(self):

        soup = BeautifulSoup(
            self.invalid_html,
            "html.parser"
        )

        item = soup.find(
            "div",
            class_="collection-card"
        )

        result = extract_store_products(item)

        self.assertIsNone(result)

    @patch("utils.extract.fetching_content")
    def test_scrape_store_products(self, mock_fetching):

        mock_fetching.return_value = self.sample_html

        result = scrape_store_products(
            "https://fashion-studio.dicoding.dev/",
            delay=0,
            max_pages=1
        )

        self.assertIsInstance(
            result,
            list
        )

        self.assertGreater(
            len(result),
            0
        )

        self.assertIn(
            "Title",
            result[0]
        )

        self.assertIn(
            "Price",
            result[0]
        )


if __name__ == "__main__":
    unittest.main()